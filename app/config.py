from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    POKEAPI_URL: str = "https://pokeapi.co/api/v2/pokemon?limit=1000"

    class Config:
        env_file = ".env"

settings = Settings()
