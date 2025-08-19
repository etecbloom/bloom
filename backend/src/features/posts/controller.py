from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from infra.database import get_db
from . import service, schema
from infra.auth import get_current_user

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/", response_model=schema.PostResponse)
async def create_post(
    post: schema.PostCreate,
    db: AsyncSession = Depends(get_db)
):
    return await service.create_post(db, post, user)

@router.get("/", response_model=list[schema.PostResponse])
async def list_posts(db: AsyncSession = Depends(get_db)):
    return await service.get_posts(db)