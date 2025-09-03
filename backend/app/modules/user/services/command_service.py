from app.modules.user.schema import CreateUserSchema, UserPartialUpdateSchema
from app.modules.user.repository import UserRepository
from app.modules.user.model import User

from app.core.security import hash_password

class UserCommandService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def create_user(self, user_data: CreateUserSchema) -> User:
        if await self.user_repo.get_by_username(user_data.username):
            raise ValueError("Username já existe")
        
        user_dict = user_data.model_dump()
        user_dict["hashed_password"] = hash_password(user_dict.pop("password"))

        return await self.user_repo.create_user(user_dict)
    
    async def delete_by_id(self, id: int) -> bool:
        user = await self.user_repo.get_by_id(id)

        if not user:
            return False
        
        await self.user_repo.delete_by_id(user)
        return True
    
    async def patch_user(self, id: int, patch_data: UserPartialUpdateSchema) -> User | None:
        updates = patch_data.model_dump(exclude_unset=True)

        if "password" in updates:
            updates["password"] = hash_password(updates["password"])

        updated_user = await self.user_repo.patch_method(id, updates)
        if not updated_user:
            raise ValueError(f"User not found with id: {id}")

        return updated_user
    