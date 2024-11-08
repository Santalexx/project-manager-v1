# Importación de módulos necesarios
from rest_framework import serializers  # Importa clases base para serialización
from .models import Task  # Importa el modelo Task
from django.contrib.auth import get_user_model  # Función para obtener el modelo de Usuario
from django.utils import timezone  # Para manejar fechas y zonas horarias

# Obtiene el modelo de Usuario activo en el proyecto
User = get_user_model()

# Serializador principal para el modelo Task
class TaskSerializer(serializers.ModelSerializer):
    # Campos calculados adicionales
    assigned_to_name = serializers.SerializerMethodField()  # Nombre del usuario asignado
    project_name = serializers.SerializerMethodField()      # Nombre del proyecto
    
    class Meta:
        model = Task  # Especifica el modelo a serializar
        # Define los campos a incluir en la serialización
        fields = ('id', 'title', 'description', 'project', 'project_name',
                 'assigned_to', 'assigned_to_name', 'priority', 'status',
                 'due_date', 'created_at', 'updated_at')
        # Campos que solo son de lectura
        read_only_fields = ('id', 'created_at', 'updated_at')

    # Método para obtener el nombre del usuario asignado
    def get_assigned_to_name(self, obj):
        if obj.assigned_to:
            return f"{obj.assigned_to.first_name} {obj.assigned_to.last_name}".strip() or obj.assigned_to.username
        return None

    # Método para obtener el nombre del proyecto
    def get_project_name(self, obj):
        return obj.project.name

# Serializador específico para la creación de tareas
class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # Campos permitidos durante la creación
        fields = ('title', 'description', 'project', 'assigned_to',
                 'priority', 'status', 'due_date')

    # Método de validación personalizado
    def validate(self, data):
        # Validar que la fecha límite no sea anterior a la fecha actual
        if data['due_date'] < timezone.now().date():
            raise serializers.ValidationError(
                "La fecha límite no puede ser anterior a la fecha actual"
            )
        
        # Validar que el usuario asignado sea parte del equipo del proyecto
        if data['assigned_to'] and not data['project'].team_members.filter(id=data['assigned_to'].id).exists():
            raise serializers.ValidationError(
                "El usuario asignado debe ser parte del equipo del proyecto"
            )
        
        return data

# Serializador para listar tareas (versión resumida)
class TaskListSerializer(serializers.ModelSerializer):
    # Campos calculados adicionales
    assigned_to_name = serializers.SerializerMethodField()
    project_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Task
        # Campos incluidos en la vista de lista
        fields = ('id', 'title', 'project_name', 'assigned_to_name',
                 'priority', 'status', 'due_date')

    # Método para obtener el nombre del usuario asignado
    def get_assigned_to_name(self, obj):
        if obj.assigned_to:
            return f"{obj.assigned_to.first_name} {obj.assigned_to.last_name}".strip() or obj.assigned_to.username
        return None

    # Método para obtener el nombre del proyecto
    def get_project_name(self, obj):
        return obj.project.name

# Serializador específico para actualizar tareas
class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # Campos que se pueden actualizar
        fields = ('title', 'description', 'assigned_to',
                 'priority', 'status', 'due_date')

    # Validación específica para el campo assigned_to
    def validate_assigned_to(self, value):
        if value and not self.instance.project.team_members.filter(id=value.id).exists():
            raise serializers.ValidationError(
                "El usuario asignado debe ser parte del equipo del proyecto"
            )
        return value