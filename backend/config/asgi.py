"""
Archivo de configuración ASGI para el proyecto Django.

ASGI (Asynchronous Server Gateway Interface) es el estándar para aplicaciones 
web asíncronas en Python. Permite manejar conexiones websockets, HTTP de larga 
duración y otros protocolos asíncronos.

Este archivo expone la variable 'application' a nivel de módulo, que es 
necesaria para los servidores web compatibles con ASGI.

Para más información sobre este archivo, consulta:
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

# Importación de módulos necesarios
import os  # Módulo para interactuar con el sistema operativo

# Importa la función que crea la aplicación ASGI de Django
from django.core.asgi import get_asgi_application

# Configura la variable de entorno que especifica el módulo de configuración
# Esta línea le dice a Django dónde encontrar la configuración principal
# 'config.settings' es la ruta al archivo settings.py del proyecto
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Crea y asigna la aplicación ASGI
# Esta variable 'application' es la que buscarán los servidores ASGI
# para ejecutar tu aplicación Django
application = get_asgi_application()