# Banking Clean API 🏦

Backend financiero desarrollado con **FastAPI** y **Clean Architecture**. Una API moderna y escalable para gestionar usuarios y cuentas bancarias.

---

## 📋 Tabla de Contenidos

- [📋 Descripción del Proyecto](#-descripción-del-proyecto)
- [🎯 Características Principales](#-características-principales)
- [📦 Requisitos Previos](#-requisitos-previos)
- [🚀 Instalación del Entorno](#-instalación-del-entorno)
- [📚 Instalación de Dependencias](#-instalación-de-dependencias)
- [⚙️ Configuración del Ambiente](#️-configuración-del-ambiente)
- [🗂️ Estructura del Proyecto](#️-estructura-del-proyecto)
- [📡 Documentación de la API](#-documentación-de-la-api)
- [🎮 Cómo Ejecutar la Aplicación](#-cómo-ejecutar-la-aplicación)
- [🧪 Testing y Verificación](#-testing-y-verificación)
- [📝 Sistema de Logging](#-sistema-de-logging)
- [🏗️ Arquitectura: Clean Architecture](#️-arquitectura-clean-architecture)
- [🔒 Seguridad y Manejo de Errores](#-seguridad-y-manejo-de-errores)
- [🤝 Contribuir](#-contribuir)
- [📄 Licencia](#-licencia)

---

## 📋 Descripción del Proyecto

## 📋 Descripción del Proyecto

Banking Clean API es una aplicación backend que implementa un sistema de gestión bancaria siguiendo principios de **Clean Architecture**. Incluye una capa de dominio independiente (`app/domain/`) para modelar entidades y reglas de negocio, separada de la infraestructura de persistencia. Proporciona endpoints RESTful para operaciones de gestión de usuarios incluyendo creación, consulta individual y listado completo.

**Versión:** 1.0.0

---

## 🎯 Características Principales

- ✅ Gestión completa de usuarios (CRUD)
- ✅ Creación, consulta por ID y listado de usuarios
- ✅ Validación de email único
- ✅ Verificación automática de conexión a base de datos
- ✅ Inicio seguro del servidor con validación de BD
- ✅ Manejo robusto de errores de base de datos
- ✅ Sistema de logging avanzado y configurable
- ✅ Logging de requests HTTP con IP de cliente
- ✅ Logging detallado de operaciones de BD
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

### 1. Crear archivo `.env` (Obligatorio)

Copia el contenido del archivo `.env.example` y configúralo según tu entorno:

```bash
cp .env.example .env
```

**Contenido mínimo requerido:**
```env
DATABASE_URL=sqlite:///./bank_app.db
```

### 2. Configurar Base de Datos

**Opción 1: SQLite (Desarrollo - Recomendado)**
```
DATABASE_URL=sqlite:///./bank_app.db
```
- ✅ No requiere instalación adicional
- ✅ Base de datos se crea automáticamente
- ✅ Ideal para desarrollo y testing

**Opción 2: MySQL (Producción)**
```
DATABASE_URL=mysql+pymysql://usuario:contraseña@host:puerto/nombre_base_datos
```
- ⚠️ Requiere MySQL server ejecutándose
- ⚠️ La base de datos debe existir previamente
- ⚠️ Credenciales deben ser correctas

**Opción 3: PostgreSQL**
```
DATABASE_URL=postgresql://usuario:contraseña@host:puerto/nombre_base_datos
```

### ⚠️ Verificación de Conexión

La aplicación **verifica automáticamente** la conexión a la base de datos al iniciar:

- ✅ **SQLite**: Se crea automáticamente si no existe
- ✅ **MySQL/PostgreSQL**: Debe existir y ser accesible
- ❌ **Si falla**: El servidor NO se inicia y muestra mensaje de error claro

### Variables de Entorno Disponibles

```env
# Base de datos (OBLIGATORIO)
DATABASE_URL=sqlite:///./bank_app.db

# Aplicación (opcionales)
PROJECT_NAME=Bank App API
VERSION=1.0.0
```
```

---

## 🗂️ Estructura del Proyecto

```
bank_app_api/
├── app/                          # 📁 Aplicación principal
│   ├── __init__.py
│   ├── main.py                   # 🚀 Punto de entrada de la aplicación
│   │
│   ├── api/                      # 🌐 Capa de Presentación (Controllers/Routers)
│   │   ├── __init__.py
│   │   └── user_router.py        # 👥 Rutas de usuarios
│   │
│   ├── core/                     # ⚙️ Configuración central
│   │   ├── __init__.py
│   │   ├── config.py             # 🔧 Configuración general
│   │   └── logging_config.py     # 📝 Configuración de logging
│   │
│   ├── domain/                   # 🎯 Capa de Dominio (Modelo y reglas de negocio)
│   │   ├── __init__.py
│   │   ├── user.py               # 👤 Entidad de dominio User
│   │   └── repositories.py       # 📋 Interfaz de repositorio de usuario
│   │
│   ├── infrastructure/           # 🏗️ Capa de Infraestructura
│   │   ├── __init__.py
│   │   ├── database.py           # 🗄️ Configuración de BD
│   │   └── models/               # 📊 Modelos ORM de SQLAlchemy
│   │       ├── __init__.py
│   │       ├── user_entity.py    # 👤 Modelo de Usuario
│   │       └── account_entity.py # 💳 Modelo de Cuenta
│   │
│   ├── repositories/             # 💾 Capa de Acceso a Datos
│   │   ├── __init__.py
│   │   └── user_repository.py    # 🔍 Operaciones de BD para usuarios
│   │
│   ├── schemas/                  # 📋 Esquemas Pydantic (DTOs)
│   │   ├── __init__.py
│   │   └── user_schema.py        # ✅ Validación de entrada/salida de usuarios
│   │
│   └── services/                 # 🔧 Capa de Lógica de Negocio
│       ├── __init__.py
│       └── user_service.py       # 👥 Servicios de usuario
│
├── test/                         # 🧪 Tests
│   ├── __init__.py
│   └── test_user_service.py      # 🧪 Pruebas del servicio de usuarios
│
├── .env                          # 🔐 Variables de entorno (NO commitar)
├── .env.example                  # 📄 Ejemplo de variables de entorno
├── .gitignore                    # 🚫 Archivos ignorados por Git
├── helper.txt                    # 📄 Archivo auxiliar
├── README.md                     # 📖 Este archivo
├── requirements.txt              # 📦 Dependencias Python
├── bank_app.db                   # 🗄️ Base de datos SQLite (generada)
└── test_setup.py                 # 🧪 Script de verificación de configuración
```

### 📋 Descripción de Capas

#### 1. **🌐 API (Controllers/Routers)**
- Maneja las solicitudes HTTP entrantes
- Valida parámetros de entrada y formatea respuestas
- Coordina entre la lógica de negocio y las respuestas HTTP
- **Ubicación:** `app/api/`

#### 2. **🔧 Services (Lógica de Negocio)**
- Contiene la lógica de negocio pura
- Valida reglas de negocio específicas
- Coordina operaciones entre múltiples repositorios
- **Ubicación:** `app/services/`

#### 3. **💾 Repositories (Acceso a Datos)**
- Encapsula todas las operaciones de base de datos
- Abstrae el ORM específico (SQLAlchemy)
- Facilita el testing con mocks
- **Ubicación:** `app/repositories/`

#### 4. **🎯 Domain (Modelo de Dominio)**
- Contiene entidades de negocio y reglas del dominio
- Define interfaces abstractas (repositorios)
- Mantiene la lógica independiente de la infraestructura
- **Ubicación:** `app/domain/`

#### 5. **🏗️ Infrastructure (Configuración Técnica)**
- Configuración de conexiones a base de datos
- Definición de modelos ORM
- Componentes técnicos de bajo nivel
- **Ubicación:** `app/infrastructure/`

#### 6. **📋 Schemas (Validación de Datos)**
- DTOs (Data Transfer Objects) con Pydantic
- Validación de entrada y salida de datos
- Serialización/deserialización automática
- **Ubicación:** `app/schemas/`

#### 7. **⚙️ Core (Configuración Central)**
- Configuraciones globales de la aplicación
- Sistema de logging centralizado
- Variables de entorno y settings
- **Ubicación:** `app/core/`

---

## 📡 Documentación de la API

### 🌐 Endpoints Disponibles

#### 👤 Gestión de Usuarios

##### **Crear Usuario**
```http
POST /users/
Content-Type: application/json

{
  "email": "usuario@example.com",
  "name": "Juan",
  "surname": "Pérez"
}
```

**✅ Respuesta Exitosa (201):**
```json
{
  "id": 1,
  "email": "usuario@example.com",
  "name": "Juan",
  "surname": "Pérez",
  "created_at": "2026-04-26T10:30:00"
}
```

**❌ Posibles Errores:**
- `400 Bad Request`: Datos faltantes o inválidos
- `409 Conflict`: Email ya registrado
- `422 Unprocessable Entity`: Error de validación de datos
- `500 Internal Server Error`: Error interno del servidor

##### **Obtener Usuario por ID**
```http
GET /users/{user_id}
```

**Parámetros:**
- `user_id` (integer, requerido): ID del usuario a consultar

**✅ Respuesta Exitosa (200):**
```json
{
  "id": 1,
  "email": "usuario@example.com",
  "name": "Juan",
  "surname": "Pérez",
  "created_at": "2026-04-26T10:30:00"
}
```

**❌ Posibles Errores:**
- `400 Bad Request`: ID inválido (no es un número positivo)
- `404 Not Found`: Usuario no encontrado
- `500 Internal Server Error`: Error interno del servidor

##### **Obtener Todos los Usuarios**
```http
GET /users/
```

**✅ Respuesta Exitosa (200):**
```json
[
  {
    "id": 1,
    "email": "usuario1@example.com",
    "name": "Juan",
    "surname": "Pérez",
    "created_at": "2026-04-26T10:30:00"
  },
  {
    "id": 2,
    "email": "usuario2@example.com",
    "name": "María",
    "surname": "García",
    "created_at": "2026-04-26T11:00:00"
  }
]
```

**❌ Posibles Errores:**
- `500 Internal Server Error`: Error interno del servidor

##### **Contar Usuarios**
```http
GET /users/count
```

**✅ Respuesta Exitosa (200):**
```json
{
  "count": 2,
  "message": "Total de usuarios registrados: 2"
}
```

**❌ Posibles Errores:**
- `500 Internal Server Error`: Error interno del servidor

#### 🏥 Health Check
```http
GET /
```

**✅ Respuesta Exitosa (200):**
```json
{
  "status": "healthy",
  "message": "Banking Clean API is running",
  "timestamp": "2026-04-26T12:00:00Z"
}
```

### 📖 Documentación Interactiva

Una vez ejecutada la aplicación, accede a la documentación interactiva:

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

---

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

---

## 🧪 Testing y Verificación

### Verificar Instalación
```bash
python test_setup.py
```

Este script verifica:
- ✅ Configuración de variables de entorno
- ✅ Sistema de logging configurado
- ✅ Conexión a la base de datos
- ✅ Importación correcta de la aplicación

### Resultado Esperado
```
INFO: 🧪 Ejecutando pruebas de verificación...
INFO: Probando: Configuración
INFO: ✅ Configuración cargada: Bank App API
INFO: Probando: Sistema Logging
INFO: ✅ Sistema de logging configurado correctamente
INFO: Probando: Conexión BD
INFO: ✅ Conexión a la base de datos exitosa
INFO: Probando: Importación App
INFO: ✅ Aplicación importada correctamente
INFO: ✅ Todas las pruebas pasaron (4/4)
INFO: 🚀 La aplicación está lista para ejecutarse
```

## 📊 Sistema de Logging

La aplicación incluye un sistema de logging avanzado y configurable:

### Niveles de Logging
- **DEBUG**: Información detallada para desarrollo
- **INFO**: Información general de operaciones
- **WARNING**: Advertencias que no detienen la ejecución
- **ERROR**: Errores que requieren atención

### Logging por Capa

#### 1. **Router (API)**
```log
INFO: GET /users/1 - Consultando usuario desde IP: 192.168.1.100
INFO: Usuario 1 consultado exitosamente: user@example.com
```

#### 2. **Servicio (Business Logic)**
```log
INFO: Obtenidos 5 usuarios
WARNING: Usuario no encontrado: 999
```

#### 3. **Repositorio (Data Access)**
```log
DEBUG: Buscando usuario por ID: 1
DEBUG: Usuario encontrado: ID 1 - user@example.com
INFO: Usuario creado exitosamente: user@example.com (ID: 1)
```

#### 4. **Base de Datos**
```log
INFO: 🔍 Verificando conexión a la base de datos...
INFO: ✅ Conexión a la base de datos exitosa
```

---

## 📝 Sistema de Logging

### Configuración de Logging

Para cambiar el nivel de logging, modifica el archivo `app/main.py`:

```python
setup_logging(log_level="DEBUG")  # Para desarrollo
setup_logging(log_level="INFO")   # Para producción
```

### Logging a Archivo

Para guardar logs en archivo:

```python
setup_logging(log_level="INFO", log_file="logs/app.log")
```

### Ejemplos de Logs

#### Inicio de la Aplicación
```
INFO: 🚀 Iniciando Banking Clean API...
INFO: 🔍 Verificando conexión a la base de datos...
INFO: ✅ Conexión a la base de datos exitosa
INFO: ✅ Verificaciones completadas. Iniciando servidor...
```

#### Operaciones HTTP
```
INFO: POST /users - Creando usuario: user@example.com desde IP: 192.168.1.100
INFO: Usuario registrado exitosamente: user@example.com
INFO: GET /users/1 - Consultando usuario desde IP: 192.168.1.100
INFO: Usuario 1 consultado exitosamente: user@example.com
INFO: GET /users - Listando todos los usuarios desde IP: 192.168.1.100
INFO: Listado de usuarios exitoso: 3 usuarios retornados
```

#### Operaciones de Base de Datos
```
DEBUG: Buscando usuario por email: user@example.com
DEBUG: Usuario encontrado: user@example.com (ID: 1)
DEBUG: Creando usuario en BD: newuser@example.com
INFO: Usuario creado exitosamente: newuser@example.com (ID: 2)
```

#### Errores
```
WARNING: Usuario no encontrado: 999
ERROR: Error de base de datos al crear usuario duplicate@example.com: (1062, "Duplicate entry")
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

## 🐛 Troubleshooting

### Problemas Comunes de Base de Datos

#### ❌ "Access denied for user" (MySQL)
```
sqlalchemy.exc.OperationalError: (1045, "Access denied for user 'root'@'localhost'")
```

**Soluciones:**
1. Verificar credenciales en `.env`
2. Crear usuario en MySQL:
   ```sql
   CREATE USER 'usuario'@'localhost' IDENTIFIED BY 'contraseña';
   GRANT ALL PRIVILEGES ON nombre_base_datos.* TO 'usuario'@'localhost';
   FLUSH PRIVILEGES;
   ```
3. Asegurar que MySQL esté ejecutándose

#### ❌ "Can't connect to MySQL server"
```
sqlalchemy.exc.OperationalError: (2003, "Can't connect to MySQL server")
```

**Soluciones:**
1. Verificar que MySQL esté instalado y ejecutándose
2. Verificar puerto (default: 3306)
3. Verificar host (localhost vs 127.0.0.1)

#### ❌ "Database does not exist" (MySQL/PostgreSQL)
```
sqlalchemy.exc.OperationalError: (1049, "Unknown database 'nombre_bd'")
```

**Soluciones:**
1. Crear la base de datos manualmente:
   ```sql
   CREATE DATABASE nombre_base_datos;
   ```

#### ✅ Verificar Conexión
```bash
# Para MySQL
mysql -u usuario -p nombre_base_datos -e "SELECT 1"

# Para PostgreSQL
psql -U usuario -d nombre_base_datos -c "SELECT 1"
```

### Logs de Depuración

La aplicación registra logs detallados. Para ver más información:
```bash
uvicorn app.main:app --reload --log-level debug
```

### Verificar Variables de Entorno
```bash
# Linux/Mac
echo $DATABASE_URL

# Windows PowerShell
echo $env:DATABASE_URL
```

---

## 🔒 Seguridad y Manejo de Errores

### Verificación de Base de Datos

La aplicación implementa **verificación automática** de conexión a la base de datos:

- ✅ **Inicio seguro**: Verifica conexión antes de iniciar el servidor
- ✅ **Mensajes claros**: Errores específicos para diferentes tipos de problemas
- ✅ **Logging detallado**: Registra todas las operaciones de BD
- ✅ **Rollback automático**: Transacciones se revierten en caso de error

### Mejores Prácticas Implementadas

1. **Validación de configuración**
   - Variables de entorno validadas con Pydantic
   - Mensajes de error específicos para configuración inválida

2. **Manejo de errores de base de datos**
   - Captura específica de errores de SQLAlchemy
   - Logging de errores con contexto
   - Respuestas HTTP apropiadas (400, 404, 500)

3. **Gestión de transacciones**
   - Commits explícitos en operaciones de escritura
   - Rollback automático en caso de error
   - Sesiones de BD manejadas correctamente

### Recomendaciones

1. **Variables de entorno**
   - Nunca commits `.env` en Git
   - Usa archivos `.env.example` con valores dummy

2. **Contraseñas**
   - Hashea las contraseñas con bcrypt
   - Usa JWT para autenticación

3. **CORS**
   - Configura CORS según necesidad

4. **HTTPS**
   - Usa HTTPS en producción

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Para contribuir:

### 📋 Proceso de Contribución

1. **Fork** el proyecto
2. **Crea** una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. **Abre** un Pull Request

### 🧪 Guías de Desarrollo

- Sigue los principios de **Clean Architecture**
- Mantén la **separación de capas**
- Agrega **tests** para nuevas funcionalidades
- Actualiza la **documentación** según sea necesario
- Usa **commits descriptivos**

### 📝 Estándares de Código

- **Python**: PEP 8
- **Commits**: Conventional Commits
- **Documentación**: Actualizar README y docstrings
- **Tests**: Cobertura mínima del 80%

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

## 📞 Soporte

Si tienes preguntas o problemas:

- 📧 **Email**: [tu-email@example.com]
- 🐛 **Issues**: [GitHub Issues](https://github.com/tu-usuario/bank_app_api/issues)
- 📖 **Documentación**: [Wiki del proyecto](https://github.com/tu-usuario/bank_app_api/wiki)

---

⭐ **¡Si te gusta este proyecto, dale una estrella en GitHub!** ⭐

5. **Base de datos**
   - Para desarrollo: SQLite
   - Para producción: MySQL/PostgreSQL con credenciales seguras

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
