import os

from dotenv import load_dotenv


load_dotenv()


class Config:
    POSTGRES_PORT: int = 5432
    SCHEME: str = "postgresql+asyncpg"
    HOST_NETWORK: str = "host.docker.internal"
    SQLALCHEMY_DATABASE_URI: str = (
        f"{SCHEME}"
        "://"
        f"{os.getenv('POSTGRES_USER')}"
        ":"
        f"{os.getenv('POSTGRES_PASSWORD')}"
        "@"
        f"{HOST_NETWORK}"
        ":"
        f"{POSTGRES_PORT}"
        "/"
        f"{os.getenv('POSTGRES_DB')}"
    )
