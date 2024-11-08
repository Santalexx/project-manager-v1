# Importación de módulos necesarios
from rest_framework import viewsets, permissions  # Importa clases base de DRF para vistas y permisos
from django.contrib.auth import get_user_model   # Función para obtener el modelo de Usuario
from .serializers import UserSerializer          # Importa el serializador de Usuario

# Obtiene el modelo de Usuario activo en el proyecto
User = get_user_model()

# Definición de la vista principal para el modelo User
class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar todas las operaciones CRUD de Usuario.
    ModelViewSet proporciona automáticamente las siguientes operaciones:
    
    - list: GET /users/ (listar todos los usuarios)
    - create: POST /users/ (crear un nuevo usuario)
    - retrieve: GET /users/{id}/ (obtener un usuario específico)
    - update: PUT /users/{id}/ (actualizar un usuario completo)
    - partial_update: PATCH /users/{id}/ (actualizar parcialmente un usuario)
    - destroy: DELETE /users/{id}/ (eliminar un usuario)
    """
    
    # Define el conjunto de objetos base para la vista
    # Obtiene todos los usuarios de la base de datos
    queryset = User.objects.all()
    
    # Especifica el serializador que se utilizará para convertir 
    # objetos User a JSON y viceversa
    serializer_class = UserSerializer
    
    # Define los permisos requeridos para acceder a la vista
    # IsAuthenticated requiere que el usuario esté autenticado
    # para realizar cualquier operación
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Sobrescribe el método get_queryset para personalizar 
        la consulta de objetos User.
        
        Returns:
            QuerySet: Todos los objetos User en la base de datos
        """
        return User.objects.all()