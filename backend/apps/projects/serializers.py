# Importación de módulos necesarios
from rest_framework import serializers  # Importa las clases base para serialización
from .models import Project  # Importa el modelo Project
from apps.tasks.serializers import TaskSerializer  # Importa el serializador de tareas
from django.contrib.auth import get_user_model  # Función para obtener el modelo de Usuario

# Obtiene el modelo de Usuario activo en el proyecto
User = get_user_model()

# Serializador principal para el modelo Project
class ProjectSerializer(serializers.ModelSerializer):
    # Campos adicionales personalizados
    tasks = TaskSerializer(many=True, read_only=True)  # Anida el serializador de tareas
    manager_name = serializers.SerializerMethodField()  # Campo calculado para el nombre del gerente
    team_members_detail = serializers.SerializerMethodField()  # Campo calculado para detalles del equipo
    
    # Configuración del serializador
    class Meta:
        model = Project  # Especifica el modelo a serializar
        # Lista de campos a incluir en la serialización
        fields = ('id', 'name', 'description', 'start_date', 'end_date',
                 'status', 'manager', 'manager_name', 'team_members',
                 'team_members_detail', 'tasks', 'created_at', 'updated_at')
        # Campos que solo son de lectura
        read_only_fields = ('id', 'created_at', 'updated_at')

    # Método para obtener el nombre completo del gerente
    def get_manager_name(self, obj):
        return f"{obj.manager.first_name} {obj.manager.last_name}".strip() or obj.manager.username

    # Método para obtener detalles de los miembros del equipo
    def get_team_members_detail(self, obj):
        return [
            {
                'id': member.id,
                'name': f"{member.first_name} {member.last_name}".strip() or member.username,
                'role': member.role
            }
            for member in obj.team_members.all()
        ]

# Serializador para listar proyectos (versión resumida)
class ProjectListSerializer(serializers.ModelSerializer):
    # Campos adicionales personalizados
    manager_name = serializers.SerializerMethodField()  # Nombre del gerente
    tasks_count = serializers.SerializerMethodField()   # Contador de tareas
    
    class Meta:
        model = Project
        # Campos incluidos en la vista de lista
        fields = ('id', 'name', 'status', 'manager_name', 
                 'start_date', 'end_date', 'tasks_count')

    # Método para obtener el nombre del gerente
    def get_manager_name(self, obj):
        return f"{obj.manager.first_name} {obj.manager.last_name}".strip() or obj.manager.username

    # Método para contar las tareas del proyecto
    def get_tasks_count(self, obj):
        return obj.tasks.count()

# Serializador específico para la creación de proyectos
class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # Campos permitidos durante la creación
        fields = ('name', 'description', 'start_date', 'end_date',
                 'manager', 'team_members')

    # Método de validación personalizado
    def validate(self, data):
        # Verifica que la fecha de inicio sea anterior a la fecha de finalización
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError(
                "La fecha de inicio no puede ser posterior a la fecha de finalización"
            )
        return data