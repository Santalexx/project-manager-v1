# Importación de módulos necesarios
from django.contrib.auth.models import AbstractUser  # Clase base para el modelo de usuario
from django.db import models  # Modelos de Django

# Definición del modelo de usuario personalizado
class CustomUser(AbstractUser):
    """
    Modelo de usuario personalizado que extiende AbstractUser de Django
    AbstractUser ya incluye campos como:
    - username
    - first_name
    - last_name
    - email
    - is_staff
    - is_active
    - date_joined
    """
    
    # Definición de las opciones de roles disponibles
    # Tupla de tuplas con formato (valor_guardado, valor_mostrado)
    ROLES = (
        ('ADMIN', 'Administrador'),  # Rol de administrador del sistema
        ('PM', 'Project Manager'),   # Rol de gerente de proyecto
        ('DEV', 'Developer'),        # Rol de desarrollador
        ('CLIENT', 'Cliente'),       # Rol de cliente
    )
    
    # Campos personalizados adicionales
    # Campo para el rol del usuario
    role = models.CharField(
        max_length=20,      # Longitud máxima del string
        choices=ROLES,      # Opciones disponibles definidas en ROLES
        default='DEV'       # Valor por defecto
    )
    
    # Campo para el número de teléfono
    phone = models.CharField(
        max_length=15,     # Longitud máxima para números de teléfono
        blank=True         # Permite que el campo esté vacío en formularios
    )
    
    # Campo para la imagen de perfil
    profile_image = models.ImageField(
        upload_to='profiles/',  # Directorio donde se guardarán las imágenes
        blank=True,            # Permite que el campo esté vacío en formularios
        null=True             # Permite valores NULL en la base de datos
    )
    
    # Campo para el departamento del usuario
    department = models.CharField(
        max_length=100,    # Longitud máxima del string
        blank=True         # Permite que el campo esté vacío
    )
    
    # Campos de auditoría
    created_at = models.DateTimeField(
        auto_now_add=True  # Se establece automáticamente al crear el usuario
    )
    updated_at = models.DateTimeField(
        auto_now=True      # Se actualiza automáticamente al modificar el usuario
    )

    # Configuración adicional del modelo
    class Meta:
        verbose_name = 'Usuario'          # Nombre singular para el admin
        verbose_name_plural = 'Usuarios'  # Nombre plural para el admin