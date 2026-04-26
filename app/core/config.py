import logging
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import ValidationError, field_validator

logger = logging.getLogger(__name__)

class Settings(BaseSettings):
    # FastAPI buscará estas variables en el entorno o en el archivo .env
    DATABASE_URL: str
    PROJECT_NAME: str = "Bank App API"
    VERSION: str = "1.0.0"

    # Configuración para leer el archivo .env
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @field_validator('DATABASE_URL')
    @classmethod
    def validate_database_url(cls, v: str) -> str:
        if not v:
            raise ValueError("DATABASE_URL no puede estar vacío")

        # Validar que tenga un esquema válido
        valid_schemes = ['sqlite://', 'mysql+pymysql://', 'postgresql://']
        if not any(v.startswith(scheme) for scheme in valid_schemes):
            raise ValueError(
                f"DATABASE_URL debe comenzar con uno de: {', '.join(valid_schemes)}. "
                f"Valor actual: {v}"
            )

        return v

def get_settings() -> Settings:
    """
    Obtiene la configuración con manejo de errores mejorado.
    """
    try:
        settings = Settings()
        logger.info(f"✅ Configuración cargada exitosamente: {settings.PROJECT_NAME} v{settings.VERSION}")
        logger.info(f"📊 Base de datos configurada: {settings.DATABASE_URL.split('://')[0].upper()}")
        return settings
    except ValidationError as e:
        logger.error("❌ Error en la configuración:")
        for error in e.errors():
            logger.error(f"  - {error['loc'][0]}: {error['msg']}")
        logger.error("Verifique su archivo .env o variables de entorno")
        raise
    except Exception as e:
        logger.error(f"❌ Error inesperado al cargar configuración: {e}")
        raise

# Instancia global de configuración
settings = get_settings()