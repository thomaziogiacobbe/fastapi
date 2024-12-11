from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://db:123@pgsql:5432/faculdade"
    
    class Config:
        case_sensitive = True
        
settings: Settings = Settings()