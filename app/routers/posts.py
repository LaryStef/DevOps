from typing import Annotated

from fastapi import APIRouter, Body, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import database, crud
from .schemes import Post, PostList, CreatePost


router: APIRouter = APIRouter(prefix="/posts")


@router.get(
    "/",
    responses={
        status.HTTP_200_OK: {}
    },
    description="Get all posts",
)
async def get_posts(
    session: Annotated[AsyncSession, Depends(database.get_scoped_session)]
) -> JSONResponse:
    return JSONResponse(
        content=PostList(posts=[Post(
            ID=post.id,
            title=post.title,
            content=post.content,
            author=post.author,
        ) for post in await crud.get_all_posts(session)]).model_dump_json(),
        status_code=status.HTTP_200_OK
    )


@router.post(
    "/",
    responses={
        status.HTTP_201_CREATED: {},
    },
    description="Create a new post",
)
async def create_post(
    create_post: Annotated[
        CreatePost,
        Body(),
    ],
    session: Annotated[AsyncSession, Depends(database.get_scoped_session)]
) -> JSONResponse:
    await crud.create_post(
        session,
        title=create_post.title,
        content=create_post.content,
        author=create_post.author,
    )
    return JSONResponse(
        content={},
        status_code=status.HTTP_201_CREATED
    )
