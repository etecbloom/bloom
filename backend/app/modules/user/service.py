from .schema import CreateUserSchema, ResponseUserSchema
from .repository import UserRepository
from .model import User
from app.core.security import hash_password, verify_password

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def create_user(self, user_data: CreateUserSchema) -> User:
        if await self.user_repo.get_by_username(user_data.username):
            raise ValueError("Username já existe")
        
        user_dict = user_data.model_dump()
        user_dict["hashed_password"] = hash_password(user_dict.pop("password"))

        return await self.user_repo.create_user(user_dict)
    
    async def get_by_id(self, id: int) -> ResponseUserSchema:
        user = await self.user_repo.get_by_id(id)
        if not user: 
            raise ValueError(f"User {id} NOT FOUND BY USERNAME")
        
        return ResponseUserSchema.model_validate(user)  
    
    async def get_by_username(self, username: str) -> ResponseUserSchema:
        user = await self.user_repo.get_by_username(username)
        if not user: 
            raise ValueError(f"User {username} NOT FOUND BY USERNAME")
        
        return ResponseUserSchema.model_validate(user)  
    
    async def get_by_email(self, email: str) -> ResponseUserSchema:
        user = await self.user_repo.get_by_email(email)
        if not user:
            raise ValueError(f"User {email} not found")
        
        return ResponseUserSchema.model_validate(user)

    async def delete_by_id(self, id: int) -> bool:
        user = await self.user_repo.get_by_id(id)

        if not user:
            return False
        
        await self.user_repo.delete_by_id(user)
        return True
