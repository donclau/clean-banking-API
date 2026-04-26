#!/usr/bin/env python3
"""
Script de prueba para verificar el manejo de errores de base de datos.
"""
import os
import sys
import logging
from pathlib import Path

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def test_database_connection():
    """Prueba la conexión a la base de datos"""
    try:
        from app.infrastructure.database import test_database_connection
        return test_database_connection()
    except Exception as e:
        logging.error(f"Error al probar conexión: {e}")
        return False

def test_app_import():
    """Prueba la importación de la aplicación"""
    try:
        from app.main import app
        logging.info("✅ Aplicación importada correctamente")
        return True
    except Exception as e:
        logging.error(f"❌ Error al importar aplicación: {e}")
        return False

def test_config_validation():
    """Prueba la validación de configuración"""
    try:
        from app.core.config import get_settings
        settings = get_settings()
        logging.info(f"✅ Configuración cargada: {settings.PROJECT_NAME}")
        return True
    except Exception as e:
        logging.error(f"❌ Error en configuración: {e}")
        return False

def test_logging_config():
    """Prueba la configuración de logging"""
    try:
        from app.core.logging_config import setup_logging
        setup_logging(log_level="DEBUG")
        logger = logging.getLogger("test")
        logger.debug("Test debug message")
        logger.info("Test info message")
        logging.info("✅ Sistema de logging configurado correctamente")
        return True
    except Exception as e:
        logging.error(f"❌ Error en configuración de logging: {e}")
        return False

def main():
    """Función principal de pruebas"""
    logging.info("🧪 Ejecutando pruebas de verificación...")

    # Verificar que estamos en el directorio correcto
    if not Path(".env").exists():
        logging.error("❌ Archivo .env no encontrado. Copie .env.example a .env")
        sys.exit(1)

    tests = [
        ("Configuración", test_config_validation),
        ("Sistema Logging", test_logging_config),
        ("Conexión BD", test_database_connection),
        ("Importación App", test_app_import),
    ]

    passed = 0
    total = len(tests)

    for test_name, test_func in tests:
        logging.info(f"Probando: {test_name}")
        if test_func():
            passed += 1
        logging.info("")

    if passed == total:
        logging.info(f"✅ Todas las pruebas pasaron ({passed}/{total})")
        logging.info("🚀 La aplicación está lista para ejecutarse")
        return 0
    else:
        logging.error(f"❌ {total - passed} pruebas fallaron ({passed}/{total})")
        logging.error("Verifique la configuración antes de ejecutar la aplicación")
        return 1

if __name__ == "__main__":
    sys.exit(main())