# Importación de módulos
# AppConfig es una clase base para configurar aplicaciones en Django
from django.apps import AppConfig

# Definición de la clase de configuración para la aplicación 'Projects'
# Esta clase hereda de AppConfig y permite personalizar la configuración de la app
class ProjectsConfig(AppConfig):
    # Especifica el tipo de campo automático para las claves primarias
    # BigAutoField es un campo que genera IDs únicos de 64 bits
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Define el nombre del paquete Python de la aplicación
    # Este nombre debe coincidir con la estructura de directorios del proyecto
    # 'apps.projects' indica que la app está en la carpeta 'apps/projects'
    name = 'apps.projects'
    
    # Establece el nombre legible para humanos de la aplicación
    # Este nombre aparecerá en el panel de administración de Django
    verbose_name = 'Proyectos'