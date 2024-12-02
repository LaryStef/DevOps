from typing import AsyncGenerator
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI


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


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=80,
    )
