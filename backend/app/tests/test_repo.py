import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.user.repository import UserRepository
from modules.user.model import User

@pytest.mark.asyncio
async def test_create_user(async_session: AsyncSession):
    repo = UserRepository(async_session)
    user_data = {
        "email": "test@example.com",
        "username": "testuser",
        "hashed_password": "hashed123",
        "role": "user",
        "exp_level": "beginner"
    }
    
    user = await repo.create_user(user_data)
    assert user.email == "test@example.com"
    assert user.id is not None