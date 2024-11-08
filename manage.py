#!/usr/bin/env python
"""
Utilidad de línea de comandos de Django para tareas administrativas.
Este script es el punto de entrada principal para ejecutar comandos de administración
como runserver, makemigrations, migrate, createsuperuser, etc.
"""

# Importaciones necesarias
import os   # Para interactuar con variables de entorno y sistema operativo
import sys  # Para manejar argumentos de línea de comandos


def main():
    """
    Función principal que ejecuta tareas administrativas de Django.
    
    Esta función:
    1. Configura el módulo de settings
    2. Importa y ejecuta el manejador de comandos de Django
    3. Maneja posibles errores de importación
    """
    # Configurar la variable de entorno que especifica dónde está la configuración de Django
    # Si la variable no existe, se establece 'config.settings' como valor por defecto
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    
    try:
        # Intentar importar la función que ejecuta comandos de Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Si Django no está instalado o no se encuentra, mostrar un mensaje de error útil
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Ejecutar el comando de Django especificado en los argumentos
    # sys.argv contiene la lista de argumentos pasados al script
    execute_from_command_line(sys.argv)


# Punto de entrada del script
if __name__ == "__main__":
    # Ejecutar la función principal solo si este archivo se ejecuta directamente
    main()