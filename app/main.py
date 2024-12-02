from typing import AsyncGenerator

from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.database import database
from app.routers import api


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    await database.create_db()
    yield

app: FastAPI = FastAPI(
    title="Posts API",
    lifespan=lifespan
)
app.include_router(api)


@app.get("/")
def read_root() -> str:
    return "You are at the root of the API"
