# Banking Clean API 🏦

Backend financiero desarrollado con **FastAPI** y **Clean Architecture**. Una API moderna y escalable para gestionar usuarios y cuentas bancarias.

---

## 📋 Descripción del Proyecto

Banking Clean API es una aplicación backend que implementa un sistema de gestión bancaria siguiendo principios de **Clean Architecture**. Incluye una capa de dominio independiente (`app/domain/`) para modelar entidades y reglas de negocio, separada de la infraestructura de persistencia. Proporciona endpoints RESTful para operaciones de autenticación, gestión de usuarios y cuentas bancarias.

**Versión:** 1.0.0

---

## 🎯 Características Principales

- ✅ Gestión de usuarios con validación de email
- ✅ Entidad de dominio `User` y repositorio abstracto
- ✅ Autenticación y autorización
- ✅ Gestión de cuentas bancarias
- ✅ Arquitectura limpia y escalable
- ✅ Documentación interactiva con Swagger UI
- ✅ Validación de datos con Pydantic
- ✅ ORM con SQLAlchemy
- ✅ Soporte para MySQL y SQLite

---

## 📦 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.9+** ([Descargar](https://www.python.org/downloads/))
- **pip** (gestor de paquetes de Python)
- **MySQL 8.0+** (opcional, si usas MySQL) O **SQLite** (incluido en Python)
- **Git** (para clonar el repositorio)

### Verificar instalaciones

```bash
python --version
pip --version
```

---

## 🚀 Instalación del Entorno

### 1. Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/bank_app_api.git
cd bank_app_api
```

### 2. Crear Entorno Virtual

**En Windows:**
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**En Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Actualizar pip

```bash
pip install --upgrade pip
```

---

## 📚 Instalación de Dependencias

Una vez activado el entorno virtual, instala todas las dependencias:

```bash
pip install -r requirements.txt
```

### Dependencias Principales

| Paquete | Versión | Descripción |
|---------|---------|-------------|
| FastAPI | latest | Framework web moderno |
| Uvicorn | latest | Servidor ASGI |
| SQLAlchemy | latest | ORM para base de datos |
| PyMySQL | latest | Driver para MySQL |
| Cryptography | latest | Encriptación para autenticación |
| Pydantic | latest | Validación de datos |
| python-dotenv | latest | Gestión de variables de entorno |

---

## ⚙️ Configuración del Ambiente

### 1. Crear archivo `.env`

Copia el contenido en la raíz del proyecto:

```bash
# .env
DATABASE_URL=sqlite:///./bank_app.db
# O para MySQL:
# DATABASE_URL=mysql+pymysql://usuario:contraseña@localhost:3306/bank_app
```

### 2. Configurar Base de Datos

**Opción 1: SQLite (Desarrollo)**
```
DATABASE_URL=sqlite:///./bank_app.db
```

**Opción 2: MySQL (Producción)**
```
DATABASE_URL=mysql+pymysql://usuario:contraseña@host:3306/banco_app
```

### Variables de Entorno Disponibles

```env
# Base de datos
DATABASE_URL=sqlite:///./bank_app.db

# Servidor
HOST=0.0.0.0
PORT=8000
DEBUG=True

# JWT (futuro)
SECRET_KEY=tu-clave-secreta-aqui
ALGORITHM=HS256
```

---

## 🗂️ Estructura del Proyecto

```
bank_app_api/
│
├── app/                          # Aplicación principal
│   ├── __init__.py
│   ├── main.py                  # Punto de entrada de la aplicación
│   │
│   ├── api/                     # Capa de Presentación (Controllers/Routers)
│   │   ├── __init__.py
│   │   └── user_router.py       # Rutas de usuarios
│   │
│   ├── core/                    # Configuración central
│   │   └── (vacío - preparado para configuraciones globales)
│   │
│   ├── domain/                  # Capa de Dominio (Modelo y reglas de negocio)
│   │   ├── __init__.py
│   │   ├── user.py              # Entidad de dominio User
│   │   └── repositories.py      # Interfaz de repositorio de usuario
│   │
│   ├── infrastructure/          # Capa de Infraestructura
│   │   ├── __init__.py
│   │   ├── database.py          # Configuración de BD
│   │   └── models/              # Modelos ORM de SQLAlchemy
│   │       ├── __init__.py
│   │       ├── user_entity.py   # Modelo de Usuario
│   │       └── account_entity.py # Modelo de Cuenta
│   │
│   ├── repositories/            # Capa de Acceso a Datos
│   │   └── user_repository.py   # Operaciones de BD para usuarios
│   │
│   ├── schemas/                 # Esquemas Pydantic (DTOs)
│   │   └── user_schema.py       # Validación de entrada/salida de usuarios
│   │
│   └── services/                # Capa de Lógica de Negocio
│       └── user_service.py      # Servicios de usuario
│
├── .env                         # Variables de entorno (NO commitar)
├── .gitignore                   # Archivos ignorados por Git
├── requirements.txt             # Dependencias Python
├── README.md                    # Este archivo
├── bank_app.db                  # Base de datos SQLite (generada)
└── helper.txt                   # Archivo auxiliar

```

### Descripción de Capas

#### 1. **API (Controllers/Routers)**
- Maneja las solicitudes HTTP
- Valida parámetros de entrada
- Retorna respuestas formateadas
- Ubicación: `app/api/`

#### 2. **Services (Lógica de Negocio)**
- Contiene la lógica de negocio
- Valida reglas de negocio
- Coordina entre repositorios
- Ubicación: `app/services/`

#### 3. **Repositories (Acceso a Datos)**
- Encapsula operaciones de BD
- Abstrae el ORM
- Facilita testing
- Ubicación: `app/repositories/`

#### 4. **Domain (Modelo de Dominio)**
- Contiene entidades de negocio y reglas del dominio
- Mantiene los objetos y las interfaces independientes de la infraestructura
- Permite probar la lógica sin depender de la base de datos
- Ubicación: `app/domain/`

#### 5. **Infrastructure (Configuración)**
- Base de datos y conexiones
- Modelos ORM
- Ubicación: `app/infrastructure/`

#### 6. **Schemas (Validación)**
- DTOs (Data Transfer Objects)
- Validación con Pydantic
- Ubicación: `app/schemas/`

---

## 🎮 Cómo Ejecutar la Aplicación

### Opción 1: Ejecución Directa (Desarrollo)

```bash
# Con recarga automática
python main.py
```

O directamente con uvicorn:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Opción 2: Con Uvicorn (Recomendado)

```bash
uvicorn app.main:app --reload
```

**Parámetros útiles:**
- `--reload`: Recarga automática al modificar código
- `--host 0.0.0.0`: Accesible desde cualquier interfaz
- `--port 8000`: Puerto (por defecto)

### Resultado Esperado

```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete
```

---

## 📡 Acceso a la Aplicación

Una vez iniciada, accede a:

### Swagger UI (Documentación Interactiva)
```
http://localhost:8000/docs
```

### ReDoc (Documentación Alternativa)
```
http://localhost:8000/redoc
```

### Health Check
```
GET http://localhost:8000/
```

---

## 📝 Endpoints Disponibles

### Usuarios

#### Crear Usuario
```http
POST /users/
Content-Type: application/json

{
  "email": "usuario@example.com",
  "name": "Juan",
  "surname": "Pérez"
}
```

**Respuesta (201):**
```json
{
  "id": 1,
  "email": "usuario@example.com",
  "name": "Juan",
  "surname": "Pérez",
  "created_at": "2026-04-26T10:30:00"
}
```

#### Obtener Usuario por Email
```http
GET /users/{email}
```

---

## 🏗️ Arquitectura: Clean Architecture

El proyecto implementa **Clean Architecture** con una separación clara entre la lógica de negocio y los detalles de infraestructura.

```
┌─────────────────────────────────┐
│      API / Controllers           │  ← Capa de Presentación
└─────────────────────────────────┘
              ↓
┌─────────────────────────────────┐
│      Services (Business Logic)   │  ← Lógica de Negocio
└─────────────────────────────────┘
              ↓
┌─────────────────────────────────┐
│      Domain (Modelo de Dominio)  │  ← Entidades e interfaces
└─────────────────────────────────┘
              ↓
┌─────────────────────────────────┐
│      Repositories (Data Access)  │  ← Acceso a Datos
└─────────────────────────────────┘
              ↓
┌─────────────────────────────────┐
│      Database / ORM              │  ← Infraestructura
└─────────────────────────────────┘
```

### Ventajas

- ✅ Independencia de frameworks
- ✅ Testabilidad
- ✅ Escalabilidad
- ✅ Mantenibilidad
- ✅ Flexibilidad

---

## 🧠 Patrones de diseño y arquitectura

Este proyecto aplica varios patrones de diseño importantes:

- **Clean Architecture / Onion Architecture**: separa las capas de presentación, aplicación, dominio e infraestructura. El dominio es el núcleo más estable.
- **Domain Model**: `app/domain/user.py` representa la entidad `User` como objeto de negocio independiente de la base de datos.
- **Repository Pattern**: `app/domain/repositories.py` define la interfaz del repositorio y `app/repositories/user_repository.py` la implementa. Esto permite cambiar la persistencia sin tocar la lógica de negocio.
- **Dependency Inversion**: los servicios dependen de abstracciones (`UserRepositoryInterface`) y no de implementaciones concretas.
- **DTOs / Data Transfer Objects**: los esquemas de Pydantic en `app/schemas/` separan la validación de entrada/salida de la lógica interna.
- **Single Responsibility Principle**: cada capa tiene una responsabilidad clara y única.

Estas decisiones hacen el proyecto más fácil de mantener, probar y evolucionar con nuevos casos de uso o proveedores de datos.

---

## 🧪 Testing (Futuro)

Próximamente se añadirá:

```bash
pip install pytest pytest-asyncio
pytest
```

---

## 🔒 Seguridad

### Recomendaciones

1. **Variables de entorno**
   - Nunca commits `.env` en Git
   - Usa archivos `.env.example` con valores dummy

2. **Contraseñas**
   - Hasea las contraseñas con bcrypt
   - Usa JWT para autenticación

3. **CORS**
   - Configura CORS según necesidad

4. **HTTPS**
   - Usa HTTPS en producción

---

## 📊 Base de Datos

### Tablas

#### Usuarios (users)
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_users_email (email)
);
```

#### Cuentas (accounts)
```sql
CREATE TABLE accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    account_number VARCHAR(20) NOT NULL UNIQUE,
    balance DECIMAL(15, 2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    INDEX idx_accounts_user (user_id)
);
```

---

## 🐛 Troubleshooting

### Error: "No module named 'sqlalchemy'"
```bash
pip install -r requirements.txt
```

### Error: "Access denied for user 'user'"
- Verifica las credenciales en `.env`
- Asegúrate de que MySQL está corriendo
- Usa SQLite para desarrollo

### Error: "Address already in use"
```bash
# Cambiar puerto
uvicorn app.main:app --port 8001
```

### Error: "ModuleNotFoundError"
- Activa el entorno virtual
- Verifica que estés en el directorio correcto

---

## 📚 Recursos Útiles

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

---

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver `LICENSE` para más detalles.

---

## 👤 Autor

**Claudio Rodolfo**
- GitHub: [@donclau](https://github.com/donclau)

---

## 📞 Soporte

Para reportar problemas o sugerencias, abre un issue en GitHub.

---

**Última actualización:** Abril 2026
