from app.core.db.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession 
from fastapi import Depends

from app.modules.user.services.command_service import UserCommandService
from app.modules.user.services.query_service import UserQueryService

from .repository import UserRepository

async def get_user_repository(
    session: AsyncSession = Depends(get_async_session)
) -> UserRepository:
    return UserRepository(session)

async def get_user_query_service(
    repo: UserRepository = Depends(get_user_repository)
) -> UserQueryService:
    return UserQueryService(repo)

async def get_user_command_service(
    repo: UserRepository = Depends(get_user_repository)
) -> UserCommandService:
    return UserCommandService(repo)