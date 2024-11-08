"""
Archivo de configuración WSGI para el proyecto Django.

WSGI (Web Server Gateway Interface) es el estándar Python para comunicación
entre aplicaciones web y servidores web. Este archivo configura cómo el
servidor web se comunicará con tu aplicación Django.

Este archivo expone la variable 'application' a nivel de módulo, que es 
requerida por servidores web compatibles con WSGI como Gunicorn, uWSGI, etc.

Para más información sobre este archivo, consulta:
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

# Importación de módulos necesarios
import os  # Módulo para interactuar con el sistema operativo

# Importa la función que crea la aplicación WSGI de Django
from django.core.wsgi import get_wsgi_application

# Configura la variable de entorno que especifica el módulo de configuración
# Esta línea le dice a Django dónde encontrar la configuración principal
# 'config.settings' es la ruta al archivo settings.py del proyecto
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Crea y asigna la aplicación WSGI
# Esta variable 'application' es la que buscarán los servidores WSGI
# para ejecutar tu aplicación Django
application = get_wsgi_application()