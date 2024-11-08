# Importaciones necesarias
from django.contrib import admin  # Para el panel de administración
from django.urls import path, include  # Para definir URLs
from django.conf import settings  # Para acceder a la configuración
from django.conf.urls.static import static  # Para servir archivos estáticos
from rest_framework import routers  # Router de DRF para APIs

# Importación de ViewSets
from apps.users.views import UserViewSet  # ViewSet de usuarios
from apps.projects.views import ProjectViewSet  # ViewSet de proyectos
from apps.tasks.views import TaskViewSet  # ViewSet de tareas

# Configuración del router para la API REST
# DefaultRouter crea automáticamente URLs para CRUD
router = routers.DefaultRouter()

# Registro de ViewSets en el router
# Cada register() crea automáticamente las siguientes URLs:
# - GET /users/ - Lista de usuarios
# - POST /users/ - Crear usuario
# - GET /users/{id}/ - Detalle de usuario
# - PUT /users/{id}/ - Actualizar usuario
# - PATCH /users/{id}/ - Actualizar parcialmente usuario
# - DELETE /users/{id}/ - Eliminar usuario
router.register(r'users', UserViewSet, basename='user')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'tasks', TaskViewSet, basename='task')

# Definición de patrones de URL del proyecto
urlpatterns = [
    # URL del panel de administración de Django
    path('admin/', admin.site.urls),
    
    # URLs de la API - Incluye todas las URLs generadas por el router
    path('api/', include(router.urls)),
    
    # URLs de autenticación de DRF - Proporciona formularios de login/logout
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# Configuración para servir archivos estáticos y media en desarrollo
if settings.DEBUG:
    # Añade URLs para servir archivos media
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Añade URLs para servir archivos estáticos
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)