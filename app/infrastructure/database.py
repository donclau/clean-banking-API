import os
import logging
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from app.core.config import get_settings

settings = get_settings()

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def test_database_connection() -> bool:
    """
    Verifica la conexión a la base de datos.
    Returns:
        bool: True si la conexión es exitosa, False en caso contrario
    """
    try:
        logger.info("🔍 Verificando conexión a la base de datos...")
        # Intentar crear una conexión y ejecutar una query simple
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            logger.info("✅ Conexión a la base de datos exitosa")
            return True
    except SQLAlchemyError as e:
        logger.error(f"❌ Error de conexión a la base de datos: {e}")
        return False
    except Exception as e:
        logger.error(f"❌ Error inesperado al conectar con la base de datos: {e}")
        return False

def create_database_if_not_exists():
    """
    Crea la base de datos si no existe (solo para SQLite).
    Para MySQL/PostgreSQL, la base de datos debe existir previamente.
    """
    if "sqlite" in settings.DATABASE_URL.lower():
        # Para SQLite, crear el archivo si no existe
        db_path = settings.DATABASE_URL.replace("sqlite:///", "")
        if not os.path.exists(db_path):
            logger.info(f"Creando base de datos SQLite: {db_path}")
            # Crear las tablas
            Base.metadata.create_all(bind=engine)
            logger.info("✅ Base de datos SQLite creada exitosamente")
    else:
        # Para otros motores, verificar que las tablas existan
        try:
            with engine.connect() as connection:
                # Intentar una query simple para verificar que la BD existe
                connection.execute(text("SELECT 1"))
                logger.info("Base de datos externa verificada")
        except SQLAlchemyError as e:
            logger.error(f"Error al verificar base de datos externa: {e}")
            logger.error("Asegúrese de que la base de datos existe y las credenciales son correctas")
            raise

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()