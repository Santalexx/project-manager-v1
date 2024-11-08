#!/usr/bin/env python
"""
Utilidad de línea de comandos de Django para tareas administrativas.
Este script es el punto de entrada principal para gestionar el proyecto Django.
Permite ejecutar comandos como runserver, makemigrations, migrate, etc.
"""

# Importaciones necesarias
import os          # Para interactuar con el sistema operativo
import sys         # Para acceder a argumentos de línea de comandos
from pathlib import Path  # Para manejo de rutas multiplataforma
from dotenv import load_dotenv  # Para cargar variables de entorno

def main():
    """
    Función principal que ejecuta tareas administrativas.
    Esta función:
    1. Carga variables de entorno
    2. Configura el módulo de settings
    3. Ejecuta comandos de Django
    """
    # Obtener la ruta al archivo .env
    # resolve() convierte la ruta en absoluta
    # parent obtiene el directorio que contiene este archivo
    env_path = Path(__file__).resolve().parent / '.env'
    
    # Cargar variables desde el archivo .env
    load_dotenv(env_path)

    # Configurar la variable de entorno que especifica el módulo de settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    
    try:
        # Intentar importar la función de manejo de comandos de Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Si Django no está instalado, mostrar un mensaje de error útil
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Ejecutar el comando especificado en los argumentos de línea de comandos
    execute_from_command_line(sys.argv)


# Punto de entrada del script
if __name__ == '__main__':
    # Ejecutar la función principal solo si este archivo se ejecuta directamente
    main()