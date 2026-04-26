from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # FastAPI buscará estas variables en el entorno o en el archivo .env
    DATABASE_URL: str
    PROJECT_NAME: str = "Bank App API"
    VERSION: str = "1.0.0"

    # Configuración para leer el archivo .env
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()