from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://myuser:myuser@localhost:5432/notes_ai"
    SECRET_KEY: str = "YOUR_SECRET_KEY_CHANGE_ME"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day
    OPENAI_API_KEY: str = "your_openai_api_key_here"

    class Config:
        env_file = ".env"

settings = Settings()
