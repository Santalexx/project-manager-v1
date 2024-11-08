# Importación de módulos necesarios
from django.db import models  # Importa las clases base para modelos de Django
from django.conf import settings  # Importa la configuración del proyecto Django

# Definición del modelo Project que hereda de models.Model
class Project(models.Model):
    # Definición de constantes
    # Tupla de opciones para el campo status con formato (valor_guardado, valor_mostrado)
    STATUS_CHOICES = (
        ('PLANNING', 'Planificación'),
        ('IN_PROGRESS', 'En Progreso'),
        ('ON_HOLD', 'En Pausa'),
        ('COMPLETED', 'Completado'),
        ('CANCELLED', 'Cancelado'),
    )

    # Campos del modelo
    # CharField para texto corto con longitud máxima de 200 caracteres
    name = models.CharField('Nombre', max_length=200)
    
    # TextField para texto largo sin límite de caracteres
    description = models.TextField('Descripción')
    
    # DateField para almacenar fechas
    start_date = models.DateField('Fecha de inicio')
    end_date = models.DateField('Fecha de finalización')
    
    # CharField con opciones predefinidas en STATUS_CHOICES
    status = models.CharField(
        'Estado', 
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='PLANNING'
    )
    
    # ForeignKey para relación uno a muchos con el modelo de Usuario
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Modelo de usuario definido en settings
        on_delete=models.PROTECT,  # Protege contra eliminación accidental
        related_name='managed_projects',  # Nombre para acceder a los proyectos desde el usuario
        verbose_name='Gerente del proyecto'  # Nombre legible para humanos
    )
    
    # ManyToManyField para relación muchos a muchos con el modelo de Usuario
    team_members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='assigned_projects',
        verbose_name='Miembros del equipo'
    )
    
    # Campos de auditoría automáticos
    created_at = models.DateTimeField(auto_now_add=True)  # Se establece al crear
    updated_at = models.DateTimeField(auto_now=True)      # Se actualiza al modificar

    # Clase Meta para configuraciones adicionales del modelo
    class Meta:
        verbose_name = 'Proyecto'  # Nombre singular para el admin
        verbose_name_plural = 'Proyectos'  # Nombre plural para el admin
        ordering = ['-created_at']  # Ordenamiento por defecto (más reciente primero)

    # Método string para representación legible del objeto
    def __str__(self):
        return self.name  # Retorna el nombre del proyecto como representación