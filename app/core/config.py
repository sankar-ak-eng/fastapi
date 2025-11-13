from pydantic_settings import BaseSettings

class Config(BaseSettings):
    PROJECT_NAME: str = "FastAPI Project"
    SQLALCHEMY_DATABASE_URL:str
    SECRET_KEY:True
    ALGORITHM:str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES:int = 30

    class Config:
        env_file = ".env"


config = Config()