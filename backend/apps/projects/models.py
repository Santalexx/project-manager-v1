from django.db import models
from django.conf import settings

class Project(models.Model):
    STATUS_CHOICES = (
        ('PLANNING', 'Planificación'),
        ('IN_PROGRESS', 'En Progreso'),
        ('ON_HOLD', 'En Pausa'),
        ('COMPLETED', 'Completado'),
        ('CANCELLED', 'Cancelado'),
    )

    name = models.CharField('Nombre', max_length=200)
    description = models.TextField('Descripción')
    start_date = models.DateField('Fecha de inicio')
    end_date = models.DateField('Fecha de finalización')
    status = models.CharField('Estado', max_length=20, choices=STATUS_CHOICES, default='PLANNING')
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='managed_projects',
        verbose_name='Gerente del proyecto'
    )
    team_members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='assigned_projects',
        verbose_name='Miembros del equipo'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created_at']

    def __str__(self):
        return self.name