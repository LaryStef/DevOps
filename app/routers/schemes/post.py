from typing import Annotated, TypeAlias

from pydantic import BaseModel, Field, StringConstraints


_Title: TypeAlias = Annotated[
    str,
    StringConstraints(strip_whitespace=True, min_length=1, max_length=64),
    Field(description="Title of the post")
]


_Content: TypeAlias = Annotated[
    str,
    StringConstraints(strip_whitespace=True, min_length=1, max_length=4096),
    Field(description="Content of the post")
]


_Author: TypeAlias = Annotated[
    str | None,
    StringConstraints(strip_whitespace=True, min_length=1, max_length=64),
    Field(description="Author of the post")
]

_ID: TypeAlias = Annotated[
    int,
    Field(description="ID of the post")
]


class CreatePost(BaseModel):
    title: _Title
    content: _Content
    author: _Author


class Post(CreatePost):
    ID: _ID


class PostList(BaseModel):
    posts: list[Post]
