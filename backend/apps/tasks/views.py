# Importación de módulos necesarios
from rest_framework import viewsets, permissions  # Importa clases base de DRF para vistas y permisos
from .models import Task  # Importa el modelo Task
from .serializers import TaskSerializer  # Importa el serializador de Task

# Definición de la vista principal para el modelo Task
class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar todas las operaciones CRUD de Task.
    ModelViewSet proporciona automáticamente las siguientes operaciones:
    - list: GET /tasks/ (listar todas las tareas)
    - create: POST /tasks/ (crear una nueva tarea)
    - retrieve: GET /tasks/{id}/ (obtener una tarea específica)
    - update: PUT /tasks/{id}/ (actualizar una tarea completa)
    - partial_update: PATCH /tasks/{id}/ (actualizar parcialmente una tarea)
    - destroy: DELETE /tasks/{id}/ (eliminar una tarea)
    """
    
    # Define el conjunto de objetos base para la vista
    # Obtiene todas las tareas de la base de datos
    queryset = Task.objects.all()
    
    # Especifica el serializador que se utilizará para convertir 
    # objetos Task a JSON y viceversa
    serializer_class = TaskSerializer
    
    # Define los permisos requeridos para acceder a la vista
    # IsAuthenticated requiere que el usuario esté autenticado
    # para realizar cualquier operación
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Sobrescribe el método get_queryset para personalizar 
        la consulta de objetos Task.
        
        Returns:
            QuerySet: Todos los objetos Task en la base de datos
        """
        return Task.objects.all()