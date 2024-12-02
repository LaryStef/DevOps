from fastapi import APIRouter

from . import posts


api: APIRouter = APIRouter(prefix="/api")
api.include_router(posts.router)
