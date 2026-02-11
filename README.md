# TODO API

Una API REST completa para gestión de tareas con autenticación JWT, construida con FastAPI.

**[LIVE DEMO](https://fastapi-todo-api-production.up.railway.app/docs)** - Try it now!

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Características

- ✅ CRUD completo de tareas
- ✅ Sistema de categorías
- ✅ Autenticación JWT
- ✅ Cada usuario solo ve sus propias tareas
- ✅ Filtros por prioridad y categoría
- ✅ Validaciones robustas
- ✅ Documentación automática (Swagger)
- ✅ Relaciones entre modelos

## Tecnologías

- **FastAPI** - Framework web moderno y rápido
- **SQLAlchemy** - ORM para base de datos
- **Pydantic** - Validación de datos
- **JWT** - Autenticación segura
- **SQLite** - Base de datos (desarrollo)
- **Uvicorn** - Servidor ASGI

## Requisitos

- Python 3.11 o superior
- pip

## Instalación

1. **Clonar el repositorio:**

git clone https://github.com/Elian1509/fastapi-todo-api.git
cd fastapi-todo-api


2. **Crear entorno virtual:**

python -m venv venv


3. **Activar entorno virtual:**

- Windows:

venv\Scripts\activate


- Linux/Mac:

source venv/bin/activate


4. **Instalar dependencias:**

pip install fastapi uvicorn sqlalchemy pydantic[email] python-jose[cryptography] passlib[bcrypt] python-multipart


## Uso

1. **Iniciar el servidor:**

uvicorn app.main:app --reload


2. **Acceder a la documentación:**

Abre tu navegador en: http://127.0.0.1:8000/docs

3. **Probar la API:**

- Registra un usuario en `/register`
- Haz login en `/login`
- Usa el botón "Authorize" con tus credenciales
- Crea y gestiona tus tareas

## Endpoints Principales

### Autenticación

- `POST /register` - Registrar nuevo usuario
- `POST /login` - Iniciar sesión y obtener token
- `GET /me` - Obtener información del usuario actual

### Tareas

- `GET /tasks/` - Listar todas las tareas del usuario
- `POST /tasks/` - Crear nueva tarea
- `GET /tasks/{id}` - Obtener tarea específica
- `PUT /tasks/{id}` - Actualizar tarea
- `DELETE /tasks/{id}` - Eliminar tarea

### Categorías

- `GET /category/` - Listar categorías
- `POST /category/` - Crear categoría
- `GET /category/{id}` - Obtener categoría
- `PUT /category/{id}` - Actualizar categoría
- `DELETE /category/{id}` - Eliminar categoría

## Estructura del Proyecto

fastapi-todo-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py           # Endpoints principales
│   ├── models.py         # Modelos de base de datos
│   ├── schemas.py        # Schemas de Pydantic
│   ├── crud.py           # Operaciones de base de datos
│   ├── auth.py           # Lógica de autenticación
│   ├── database.py       # Configuración de BD
│   └── exceptions.py     # Excepciones personalizadas
│
├── venv/                 # Entorno virtual (no versionado)
├── todo.db              # Base de datos SQLite (no versionado)
├── .gitignore
└── README.md


## Seguridad

- Contraseñas hasheadas con bcrypt
- Tokens JWT con expiración
- Validaciones exhaustivas de entrada
- Cada usuario solo puede acceder a sus propios recursos

## Ejemplos de Uso

### Registrar usuario:

curl -X POST "http://127.0.0.1:8000/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "password123"
  }'


### Login:

curl -X POST "http://127.0.0.1:8000/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=password123"


### Crear tarea (con token):

curl -X POST "http://127.0.0.1:8000/tasks/" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Mi primera tarea",
    "description": "Descripción de la tarea",
    "priority": "alta"
  }'


## Próximas Mejoras

- [ ] Migración a PostgreSQL
- [ ] Tests unitarios
- [ ] Dockerización
- [ ] Deploy en la nube
- [ ] Paginación avanzada
- [ ] Búsqueda de tareas

## Autor

**Elian** - [GitHub](https://github.com/Elian1509)