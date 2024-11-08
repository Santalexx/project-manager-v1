# Importaciones necesarias
import os  # Para interactuar con el sistema operativo
from pathlib import Path  # Para manejo de rutas multiplataforma
from dotenv import load_dotenv  # Para cargar variables de entorno

# Cargar variables desde archivo .env
load_dotenv()

# Configuración de rutas base
# BASE_DIR apunta al directorio raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuraciones de seguridad
SECRET_KEY = os.getenv('SECRET_KEY')  # Clave secreta desde variables de entorno
DEBUG = os.getenv('DEBUG', 'True') == 'True'  # Modo debug
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Aplicaciones instaladas
INSTALLED_APPS = [
    # Aplicaciones core de Django
    "django.contrib.admin",         # Panel de administración
    "django.contrib.auth",          # Sistema de autenticación
    "django.contrib.contenttypes",  # Framework de tipos de contenido
    "django.contrib.sessions",      # Framework de sesiones
    "django.contrib.messages",      # Framework de mensajes
    "django.contrib.staticfiles",   # Manejo de archivos estáticos
    
    # Aplicaciones de terceros
    'rest_framework.authtoken',     # Autenticación por tokens
    'rest_framework',              # Django Rest Framework
    'corsheaders',                # Manejo de CORS
    'crispy_forms',               # Mejora de formularios
    'crispy_bootstrap5',          # Integración con Bootstrap 5
    
    # Aplicaciones locales
    'apps.users.apps.UsersConfig',      # App de usuarios
    'apps.projects.apps.ProjectsConfig', # App de proyectos
    'apps.tasks.apps.TasksConfig',       # App de tareas
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",          # Seguridad
    "django.contrib.sessions.middleware.SessionMiddleware",   # Sesiones
    "corsheaders.middleware.CorsMiddleware",                 # CORS
    "django.middleware.common.CommonMiddleware",             # Común
    "django.middleware.csrf.CsrfViewMiddleware",             # Protección CSRF
    "django.contrib.auth.middleware.AuthenticationMiddleware", # Autenticación
    "django.contrib.messages.middleware.MessageMiddleware",    # Mensajes
    "django.middleware.clickjacking.XFrameOptionsMiddleware",  # Protección clickjacking
]

# Configuración de URLs
ROOT_URLCONF = "config.urls"

# Configuración de templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],  # Directorio de templates
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Configuración de WSGI
WSGI_APPLICATION = "config.wsgi.application"

# Configuración de base de datos PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'project_management'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# Configuración de Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Configuración de autenticación
AUTH_USER_MODEL = 'users.CustomUser'  # Modelo de usuario personalizado
LOGIN_REDIRECT_URL = 'home'          # Redirección después del login
LOGOUT_REDIRECT_URL = 'home'         # Redirección después del logout
LOGIN_URL = 'login'                  # URL de login

# Configuración de archivos estáticos y media
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Configuración de CORS
CORS_ALLOWED_ORIGINS = os.getenv('CORS_ALLOWED_ORIGINS', 'http://localhost:3000').split(',')
CORS_ALLOW_CREDENTIALS = True

# Configuración regional
LANGUAGE_CODE = 'es-pe'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = True

# Campo automático por defecto
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Configuración de Django Rest Framework
REST_FRAMEWORK = {
    # Clases de autenticación
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    # Clases de permisos
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    # Configuración de paginación
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}