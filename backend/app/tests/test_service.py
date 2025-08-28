import pytest
from unittest.mock import AsyncMock
from app.modules.user.service import UserService
from app.modules.user.schema import CreateUserSchema
from shared.utils import ExperienceLevel, Role
from modules.user.model import User

@pytest.mark.asyncio
async def test_create_user_success():
    mock_user = User(
        email="test@example.com",
        username="testuser",
        hashed_password="hashed_password",
        role=Role.MOTHER,
        exp_level=ExperienceLevel.YOUNG
    )
    mock_user.id = 1
    mock_repo = AsyncMock()
    mock_repo.get_by_username.return_value = None
    mock_repo.create_user.return_value = mock_user
    
    service = UserService(mock_repo)
    user_data = CreateUserSchema(
        email="test@example.com",
        username="testuser",
        password="secret123",
        role=Role.MOTHER,
        exp_level=ExperienceLevel.YOUNG
    )
    
    result = await service.create_user(user_data)
    assert result.email == "test@example.com"

    mock_repo.get_by_username.assert_called_once_with("testuser")
    mock_repo.create_user.assert_called_once()