import logging
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import SQLAlchemyError
from app.api.user_router import router as user_router
from app.infrastructure.database import test_database_connection, create_database_if_not_exists
from app.core.logging_config import setup_logging

# Configurar logging
setup_logging(log_level="INFO")

logger = logging.getLogger(__name__)

# Verificar conexión a la base de datos antes de iniciar la aplicación
logger.info("🚀 Iniciando Banking Clean API...")

if not test_database_connection():
    logger.error("❌ No se pudo conectar a la base de datos. El servidor no se iniciará.")
    logger.error("Verifique:")
    logger.error("  - Que la base de datos esté ejecutándose")
    logger.error("  - Que las credenciales en .env sean correctas")
    logger.error("  - Que la base de datos exista (para MySQL/PostgreSQL)")
    exit(1)

# Crear base de datos si es necesario (SQLite)
try:
    create_database_if_not_exists()
except Exception as e:
    logger.error(f"❌ Error al inicializar la base de datos: {e}")
    exit(1)

# Crear la aplicación FastAPI
app = FastAPI(
    title="Banking Clean API",
    description="Backend financiero con Clean Architecture",
    version="1.0.0"
)

app.include_router(user_router)

# Health check endpoint
@app.get("/")
def health_check():
    logger.info("Health check solicitado")
    return {"status": "healthy", "message": "Banking Clean API is running", "timestamp": "2026-04-26T12:00:00Z"}

# Manejadores globales de excepciones

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Manejador para excepciones HTTP conocidas"""
    logger.warning(f"HTTP {exc.status_code} en {request.url}: {exc.detail}")

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": "HTTP_EXCEPTION",
            "message": exc.detail,
            "path": str(request.url),
            "method": request.method
        }
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Manejador para errores de validación de Pydantic"""
    logger.warning(f"Error de validación en {request.url}: {exc.errors()}")

    # Crear mensaje más amigable
    errors = []
    for error in exc.errors():
        field = ".".join(str(loc) for loc in error["loc"])
        msg = error["msg"]
        errors.append(f"{field}: {msg}")

    error_message = "Errores de validación: " + "; ".join(errors)

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": "VALIDATION_ERROR",
            "message": error_message,
            "details": exc.errors(),
            "path": str(request.url),
            "method": request.method
        }
    )

@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    """Manejador para errores de base de datos"""
    logger.error(f"Error de base de datos en {request.url}: {str(exc)}")

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "DATABASE_ERROR",
            "message": "Error interno de base de datos",
            "path": str(request.url),
            "method": request.method
        }
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Manejador para cualquier excepción no manejada"""
    logger.error(f"Error inesperado en {request.url}: {str(exc)}", exc_info=True)

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "INTERNAL_SERVER_ERROR",
            "message": "Error interno del servidor",
            "path": str(request.url),
            "method": request.method
        }
    )

if __name__ == "__main__":
    import uvicorn
    logger.info("✅ Verificaciones completadas. Iniciando servidor...")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)