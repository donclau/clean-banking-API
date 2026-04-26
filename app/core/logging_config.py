import logging
import logging.config
from pathlib import Path

def setup_logging(log_level: str = "INFO", log_file: str = None):
    """
    Configura el sistema de logging de la aplicación.

    Args:
        log_level: Nivel de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Archivo donde guardar los logs (opcional)
    """
    # Configuración base
    config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'detailed': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
            'simple': {
                'format': '%(levelname)s: %(message)s'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': log_level,
                'formatter': 'simple',
                'stream': 'ext://sys.stdout'
            }
        },
        'root': {
            'level': log_level,
            'handlers': ['console']
        },
        'loggers': {
            'app': {
                'level': log_level,
                'handlers': ['console'],
                'propagate': False
            },
            'sqlalchemy': {
                'level': 'WARNING',  # Reducir ruido de SQLAlchemy
                'handlers': ['console'],
                'propagate': False
            }
        }
    }

    # Agregar handler de archivo si se especifica
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)

        config['handlers']['file'] = {
            'class': 'logging.FileHandler',
            'level': log_level,
            'formatter': 'detailed',
            'filename': str(log_path),
            'encoding': 'utf-8'
        }

        # Agregar el handler de archivo a todos los loggers
        for logger_name in config['loggers']:
            config['loggers'][logger_name]['handlers'].append('file')
        config['root']['handlers'].append('file')

    # Aplicar configuración
    logging.config.dictConfig(config)

    # Log inicial
    logger = logging.getLogger(__name__)
    logger.info(f"🔧 Logging configurado - Nivel: {log_level}")
    if log_file:
        logger.info(f"📝 Logs guardándose en: {log_file}")