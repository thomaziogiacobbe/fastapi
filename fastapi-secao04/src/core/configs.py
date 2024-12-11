from pydantic_settings import BaseSettings

from sqlalchemy.orm import DeclarativeBase

class DBBaseModel(DeclarativeBase):
    pass

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://db:123@pgsql:5432/faculdade"
    
    class Config:
        case_sensitive = True
        
settings = Settings()