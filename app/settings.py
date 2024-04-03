from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_TOKEN: str
    HOST: str 
    PORT: int
    WEBSITE_BASE_URL: str
    IMAGES_FOLDER_NAME: str 

    class Config:
        env_file = ".env"

settings = Settings()
