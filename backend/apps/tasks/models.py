from django.db import models
from django.conf import settings

class Task(models.Model):
    PRIORITY_CHOICES = (
        ('LOW', 'Baja'),
        ('MEDIUM', 'Media'),
        ('HIGH', 'Alta'),
        ('URGENT', 'Urgente'),
    )
    
    STATUS_CHOICES = (
        ('TODO', 'Por hacer'),
        ('IN_PROGRESS', 'En progreso'),
        ('REVIEW', 'En revisión'),
        ('DONE', 'Completada'),
    )

    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descripción')
    project = models.ForeignKey(
        'projects.Project',
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='Proyecto'
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='assigned_tasks',
        verbose_name='Asignado a'
    )
    priority = models.CharField(
        'Prioridad',
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='MEDIUM'
    )
    status = models.CharField(
        'Estado',
        max_length=20,
        choices=STATUS_CHOICES,
        default='TODO'
    )
    due_date = models.DateField('Fecha límite')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['-created_at']

    def __str__(self):
        return self.title