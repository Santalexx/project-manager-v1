# Importación de módulos necesarios
from django.db import models  # Importa las clases base para modelos de Django
from django.conf import settings  # Importa la configuración del proyecto Django

# Definición del modelo Task que hereda de models.Model
class Task(models.Model):
    # Definición de constantes para opciones de prioridad
    # Tupla de tuplas con formato (valor_guardado, valor_mostrado)
    PRIORITY_CHOICES = (
        ('LOW', 'Baja'),      # Prioridad baja
        ('MEDIUM', 'Media'),   # Prioridad media
        ('HIGH', 'Alta'),      # Prioridad alta
        ('URGENT', 'Urgente'), # Prioridad urgente
    )
    
    # Definición de constantes para opciones de estado
    STATUS_CHOICES = (
        ('TODO', 'Por hacer'),        # Tarea pendiente
        ('IN_PROGRESS', 'En progreso'),# Tarea en proceso
        ('REVIEW', 'En revisión'),     # Tarea en revisión
        ('DONE', 'Completada'),        # Tarea completada
    )

    # Campos básicos de la tarea
    # CharField para el título con longitud máxima de 200 caracteres
    title = models.CharField('Título', max_length=200)
    
    # TextField para descripción sin límite de caracteres
    description = models.TextField('Descripción')
    
    # Relación con el modelo Project (ForeignKey = muchos a uno)
    project = models.ForeignKey(
        'projects.Project',        # Modelo relacionado
        on_delete=models.CASCADE,  # Si se elimina el proyecto, se eliminan sus tareas
        related_name='tasks',      # Nombre para acceder a las tareas desde el proyecto
        verbose_name='Proyecto'    # Nombre legible para humanos
    )
    
    # Relación con el modelo de Usuario
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Modelo de usuario definido en settings
        on_delete=models.SET_NULL, # Si se elimina el usuario, el campo se establece como NULL
        null=True,                 # Permite que el campo sea NULL
        related_name='assigned_tasks', # Nombre para acceder a las tareas desde el usuario
        verbose_name='Asignado a'     # Nombre legible para humanos
    )
    
    # Campo para la prioridad de la tarea
    priority = models.CharField(
        'Prioridad',
        max_length=20,
        choices=PRIORITY_CHOICES,  # Usa las opciones definidas en PRIORITY_CHOICES
        default='MEDIUM'          # Valor por defecto
    )
    
    # Campo para el estado de la tarea
    status = models.CharField(
        'Estado',
        max_length=20,
        choices=STATUS_CHOICES,    # Usa las opciones definidas en STATUS_CHOICES
        default='TODO'            # Valor por defecto
    )
    
    # Campo para la fecha límite
    due_date = models.DateField('Fecha límite')
    
    # Campos de auditoría automáticos
    created_at = models.DateTimeField(auto_now_add=True)  # Se establece al crear
    updated_at = models.DateTimeField(auto_now=True)      # Se actualiza al modificar

    # Clase Meta para configuraciones adicionales del modelo
    class Meta:
        verbose_name = 'Tarea'         # Nombre singular para el admin
        verbose_name_plural = 'Tareas' # Nombre plural para el admin
        ordering = ['-created_at']     # Ordenamiento por defecto (más reciente primero)

    # Método string para representación legible del objeto
    def __str__(self):
        return self.title  # Retorna el título de la tarea como representación