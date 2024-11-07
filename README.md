# Sistema de Gestión de Proyectos

Sistema web para la gestión y seguimiento de proyectos, asignación de tareas y administración de equipos de trabajo.

## Descripción

Este sistema de gestión de proyectos proporciona una plataforma robusta para la administración de proyectos, permitiendo la creación y seguimiento de tareas, gestión de equipos y monitoreo de progreso, todo a través de una API REST escalable y segura.

## Características principales

- Sistema completo de autenticación y autorización con roles específicos
- Gestión de proyectos con estados y fechas de seguimiento
- Administración de tareas con prioridades y asignaciones
- API REST completa con endpoints para todas las operaciones
- Sistema de roles (Administrador, Project Manager, Desarrollador, Cliente)
- Validaciones y permisos basados en roles
- Estadísticas y reportes de proyectos

## Tecnologías utilizadas

- Django 5.1.2
- Django REST Framework
- PostgreSQL
- Crispy Forms con Bootstrap 5
- Sistema de autenticación por tokens

## Requisitos previos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.12.6
- PostgreSQL 15 o superior
- Git

### Instalación de PostgreSQL

1. Descarga [PostgreSQL](https://www.postgresql.org/download/)
2. Durante la instalación, anota el usuario y contraseña que configures
3. Verifica la instalación:
   ```bash
   psql --version
   ```

## Instalación del proyecto

### Para macOS/Linux

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/project-management.git
   cd project-management
   ```

2. Crea y activa el entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura la base de datos en PostgreSQL:
   ```sql
   CREATE USER tuusuario WITH PASSWORD 'tucontraseña';
   CREATE DATABASE project_management;
   GRANT ALL PRIVILEGES ON DATABASE project_management TO tuusuario;
   ```

5. Crea el archivo .env en la carpeta backend:
   ```plaintext
   SECRET_KEY=tu-clave-secreta-aqui
   DEBUG=True
   DB_NAME=project_management
   DB_USER=tuusuario
   DB_PASSWORD=tucontraseña
   DB_HOST=localhost
   DB_PORT=5432
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

6. Realiza las migraciones:
   ```bash
   cd backend
   python manage.py migrate
   ```

7. Crea un superusuario:
   ```bash
   python manage.py createsuperuser
   ```

### Para Windows

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/project-management.git
   cd project-management
   ```

2. Crea y activa el entorno virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Sigue los pasos 3-7 de la instalación para macOS/Linux

## Uso del sistema

1. Inicia el servidor:
   ```bash
   python manage.py runserver
   ```

2. Accede a las diferentes URLs:
   - Panel de administración: http://localhost:8000/admin/
   - API Root: http://localhost:8000/api/
   - Documentación API: http://localhost:8000/api/schema/

## Endpoints principales

- `/api/users/`: Gestión de usuarios
- `/api/projects/`: Gestión de proyectos
- `/api/tasks/`: Gestión de tareas
- `/api/auth/login/`: Autenticación de usuarios
- `/api/auth/register/`: Registro de usuarios

### Endpoints adicionales

- `/api/projects/{id}/statistics/`: Estadísticas del proyecto
- `/api/projects/{id}/change_status/`: Cambiar estado del proyecto
- `/api/tasks/{id}/assign/`: Asignar tarea
- `/api/tasks/{id}/change_status/`: Actualizar estado de tarea

## Estructura del proyecto

```plaintext
project_management/
├── backend/
│   ├── apps/
│   │   ├── projects/
│   │   ├── tasks/
│   │   └── users/
│   ├── config/
│   ├── static/
│   ├── media/
│   ├── templates/
│   ├── manage.py
│   └── requirements.txt
├── frontend/  # (En desarrollo)
└── README.md
```

## Roles y permisos

- **Administrador**: Acceso total al sistema
- **Project Manager**: Gestión de proyectos y equipos
- **Desarrollador**: Gestión de tareas asignadas
- **Cliente**: Visualización de proyectos asignados

## Notas importantes

- Este es un proyecto educativo/desarrollo
- La configuración actual está optimizada para desarrollo local
- Se recomienda cambiar las claves secretas antes de usar en producción

## Contribución

1. Haz un Fork del proyecto
2. Crea una rama para tu función (`git checkout -b feature/AmazingFeature`)
3. Realiza tus cambios y haz commit (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
