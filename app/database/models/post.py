from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Post(Base):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(
        Integer(),
        primary_key=True,
        autoincrement=True,
    )

    title: Mapped[str] = mapped_column(String(64))
    author: Mapped[str | None] = mapped_column(String(64), nullable=True)
    content: Mapped[str] = mapped_column(String(4096))

    def __init__(
        self,
        *,
        title: str,
        author: str | None,
        content: str,
    ) -> None:
        self.title = title
        self.content = content
        self.author = author
