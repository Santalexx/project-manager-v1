# Importación de módulos necesarios
# AppConfig es la clase base para configurar aplicaciones en Django
from django.apps import AppConfig

# Definición de la clase de configuración para la aplicación 'Tasks'
# Esta clase hereda de AppConfig y personaliza la configuración de la app
class TasksConfig(AppConfig):
    # Especifica el tipo de campo automático para las claves primarias
    # BigAutoField genera IDs únicos de 64 bits para mayor capacidad
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Define el nombre del paquete Python de la aplicación
    # 'apps.tasks' indica que la app está en el directorio 'apps/tasks'
    # Este nombre debe coincidir con la estructura de directorios
    name = 'apps.tasks'
    
    # Establece el nombre legible para humanos de la aplicación
    # 'Tareas' aparecerá en el panel de administración de Django
    verbose_name = 'Tareas'