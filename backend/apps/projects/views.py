# Importación de módulos necesarios
from rest_framework import viewsets, permissions  # Importa clases base de DRF para vistas y permisos
from .models import Project  # Importa el modelo Project
from .serializers import ProjectSerializer  # Importa el serializador de Project

# Definición de la vista principal para el modelo Project
class ProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar todas las operaciones CRUD de Project.
    ModelViewSet proporciona automáticamente:
    - list (GET /projects/)
    - create (POST /projects/)
    - retrieve (GET /projects/{id}/)
    - update (PUT /projects/{id}/)
    - partial_update (PATCH /projects/{id}/)
    - destroy (DELETE /projects/{id}/)
    """
    
    # Define el conjunto de objetos base para la vista
    queryset = Project.objects.all()
    
    # Especifica el serializador que se utilizará para convertir 
    # objetos Project a JSON y viceversa
    serializer_class = ProjectSerializer
    
    # Define los permisos requeridos para acceder a la vista
    # IsAuthenticated requiere que el usuario esté autenticado
    permission_classes = [permissions.IsAuthenticated]

    # Método para personalizar el queryset
    def get_queryset(self):
        """
        Sobrescribe el método get_queryset para personalizar 
        la consulta de objetos Project.
        
        Returns:
            QuerySet: Todos los objetos Project en la base de datos
        """
        return Project.objects.all()