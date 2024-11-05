# apps/projects/serializers.py
from rest_framework import serializers
from .models import Project
from apps.tasks.serializers import TaskSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    manager_name = serializers.SerializerMethodField()
    team_members_detail = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'start_date', 'end_date',
                 'status', 'manager', 'manager_name', 'team_members',
                 'team_members_detail', 'tasks', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_manager_name(self, obj):
        return f"{obj.manager.first_name} {obj.manager.last_name}".strip() or obj.manager.username

    def get_team_members_detail(self, obj):
        return [
            {
                'id': member.id,
                'name': f"{member.first_name} {member.last_name}".strip() or member.username,
                'role': member.role
            }
            for member in obj.team_members.all()
        ]

class ProjectListSerializer(serializers.ModelSerializer):
    manager_name = serializers.SerializerMethodField()
    tasks_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = ('id', 'name', 'status', 'manager_name', 
                 'start_date', 'end_date', 'tasks_count')

    def get_manager_name(self, obj):
        return f"{obj.manager.first_name} {obj.manager.last_name}".strip() or obj.manager.username

    def get_tasks_count(self, obj):
        return obj.tasks.count()

class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'description', 'start_date', 'end_date',
                 'manager', 'team_members')

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError(
                "La fecha de inicio no puede ser posterior a la fecha de finalización"
            )
        return data