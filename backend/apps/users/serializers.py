# Importación de módulos necesarios
from rest_framework import serializers  # Importa las clases base para serialización
from django.contrib.auth import get_user_model  # Función para obtener el modelo de Usuario activo

# Obtiene el modelo de Usuario personalizado configurado en el proyecto
User = get_user_model()

# Serializador principal para el modelo User
class UserSerializer(serializers.ModelSerializer):
    """
    Serializador general para el modelo User.
    Se usa para operaciones de lectura y actualización de usuarios existentes.
    """
    class Meta:
        model = User  # Especifica el modelo a serializar
        # Define los campos a incluir en la serialización
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 
                 'role', 'phone', 'department', 'profile_image')
        # Campos que no se pueden modificar
        read_only_fields = ('id',)

# Serializador específico para la creación de usuarios
class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializador especializado para la creación de nuevos usuarios.
    Maneja el campo de contraseña de forma segura.
    """
    # Campo adicional para la contraseña, solo escritura
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User  # Especifica el modelo a serializar
        # Define los campos necesarios para crear un usuario
        fields = ('id', 'username', 'email', 'password', 'first_name', 
                 'last_name', 'role', 'phone', 'department')

    def create(self, validated_data):
        """
        Sobrescribe el método create para manejar la contraseña correctamente.
        
        Args:
            validated_data: Diccionario con los datos validados del usuario
            
        Returns:
            User: Instancia del nuevo usuario creado
        """
        # Extrae la contraseña de los datos validados
        password = validated_data.pop('password')
        # Crea la instancia de usuario con los datos restantes
        user = User(**validated_data)
        # Establece la contraseña de forma segura (con hash)
        user.set_password(password)
        # Guarda el usuario en la base de datos
        user.save()
        return user

# Serializador para listar usuarios (versión resumida)
class UserListSerializer(serializers.ModelSerializer):
    """
    Serializador simplificado para listar usuarios.
    Incluye solo los campos más relevantes para las vistas de lista.
    """
    class Meta:
        model = User  # Especifica el modelo a serializar
        # Define solo los campos necesarios para la vista de lista
        fields = ('id', 'username', 'first_name', 'last_name', 'role')