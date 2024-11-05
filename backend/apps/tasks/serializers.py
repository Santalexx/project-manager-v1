# apps/tasks/serializers.py
from rest_framework import serializers
from .models import Task
from django.contrib.auth import get_user_model

User = get_user_model()

class TaskSerializer(serializers.ModelSerializer):
    assigned_to_name = serializers.SerializerMethodField()
    project_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'project', 'project_name',
                 'assigned_to', 'assigned_to_name', 'priority', 'status',
                 'due_date', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_assigned_to_name(self, obj):
        if obj.assigned_to:
            return f"{obj.assigned_to.first_name} {obj.assigned_to.last_name}".strip() or obj.assigned_to.username
        return None

    def get_project_name(self, obj):
        return obj.project.name

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'project', 'assigned_to',
                 'priority', 'status', 'due_date')

    def validate(self, data):
        # Validar que la fecha límite no sea anterior a la fecha actual
        from django.utils import timezone
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

class TaskListSerializer(serializers.ModelSerializer):
    assigned_to_name = serializers.SerializerMethodField()
    project_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Task
        fields = ('id', 'title', 'project_name', 'assigned_to_name',
                 'priority', 'status', 'due_date')

    def get_assigned_to_name(self, obj):
        if obj.assigned_to:
            return f"{obj.assigned_to.first_name} {obj.assigned_to.last_name}".strip() or obj.assigned_to.username
        return None

    def get_project_name(self, obj):
        return obj.project.name

class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'assigned_to',
                 'priority', 'status', 'due_date')

    def validate_assigned_to(self, value):
        if value and not self.instance.project.team_members.filter(id=value.id).exists():
            raise serializers.ValidationError(
                "El usuario asignado debe ser parte del equipo del proyecto"
            )
        return value