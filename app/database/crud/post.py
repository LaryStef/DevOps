from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import Post


async def create_post(
    session: AsyncSession,
    /,
    *,
    title: str,
    content: str,
    author: str | None = None,
) -> None:
    post: Post = Post(title=title, content=content, author=author)
    session.add(post)
    await session.commit()
    await session.refresh(post)


async def get_all_posts(session: AsyncSession, /, ) -> list[Post]:
    result: Result[tuple[Post]] = await session.execute(select(Post))
    return list(result.scalars().all())
