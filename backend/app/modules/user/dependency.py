from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession 
from .repository import UserRepository
from .service import UserService
from app.core.db.database import get_async_session

async def get_user_repository(
    session: AsyncSession = Depends(get_async_session)
) -> UserRepository:
    return UserRepository(session)

async def get_user_service(
    repo: UserRepository = Depends(get_user_repository)
) -> UserService:
    return UserService(repo)