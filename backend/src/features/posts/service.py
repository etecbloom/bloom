from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import model, schema
from infra.logger import logger

async def create_post(db: AsyncSession, post: schema.PostCreate, user):
    new_post = model.Post(
        title=post.title,
        content=post.content,
        owner_id=user.id
    )
    db.add(new_post)
    await db.commit()
    await db.refresh(new_post)

    logger.info(
        "Post criado",
        extra={"usuario": user.username, "titulo": new_post.title}
    )

    return schema.PostResponse(
        id=new_post.id,
        title=new_post.title,
        content=new_post.content,
        owner_username=user.username
    )

async def get_posts(db: AsyncSession):
    result = await db.execute(select(model.Post))
    posts = result.scalars().all()
    return [
        schema.PostResponse(
            id=p.id,
            title=p.title,
            content=p.content,
            owner_username=p.owner.username
        )
        for p in posts
    ]
