# Importación de módulos necesarios
# AppConfig es la clase base para configurar aplicaciones en Django
from django.apps import AppConfig

# Definición de la clase de configuración para la aplicación 'Users'
# Esta clase hereda de AppConfig y personaliza la configuración de la app
class UsersConfig(AppConfig):
    # Especifica el tipo de campo automático para las claves primarias
    # BigAutoField genera IDs únicos de 64 bits para mayor capacidad
    # Útil para aplicaciones que pueden tener muchos usuarios
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Define el nombre del paquete Python de la aplicación
    # 'apps.users' indica que la app está en el directorio 'apps/users'
    # Este nombre debe coincidir con la estructura de directorios del proyecto
    name = 'apps.users'
    
    # Establece el nombre legible para humanos de la aplicación
    # 'Usuarios' aparecerá en el panel de administración de Django
    # y en otros lugares donde se muestre el nombre de la app
    verbose_name = 'Usuarios'