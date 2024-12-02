import os

from dotenv import load_dotenv


load_dotenv()


class Config:
    SHCEME: str = "postgresql+asyncpg"
    POSTGRES_PORT: int = 5432
    SQLALCHEMY_DATABASE_URI: str = (
        f"{SHCEME}"
        "://"
        f"{os.getenv('POSTGRES_USER')}"
        ":"
        f"{os.getenv('POSTGRES_PASSWORD')}"
        "@"
        f"{os.getenv('HOST_NETWORK')}"
        ":"
        f"{POSTGRES_PORT}"
        "/"
        f"{os.getenv('POSTGRES_NAME')}"
    )
