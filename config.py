from pydantic_settings import BaseSettings

class Config(BaseSettings):
    """
    Notre configuration pour le Projet Todos
    """

    bind_host: str = "0.0.0.0"
    port: int = 8000
    database_url: str = "sqlite+aiosqlite:///production.db"
    test_database_url: str = "sqlite+aiosqlite:///test.db"