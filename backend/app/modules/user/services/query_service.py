from app.core.security import verify_password

from app.modules.user.schema import ResponseUserSchema, UserLoginSchema
from app.modules.user.repository import UserRepository
from app.modules.user.model import User

class UserQueryService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo
        
    async def list_all_users(self, skip: int = 0, limit: int = 10) -> list[ResponseUserSchema]:
        users = await self.user_repo.list_all_users(skip=skip, limit=limit)
        return [ResponseUserSchema.model_validate(user) for user in users]

    async def get_by_id(self, id: int) -> ResponseUserSchema:
        user = await self.user_repo.get_by_id(id)
        if not user: 
            raise ValueError(f"User {id} NOT FOUND BY ID")
        
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
    
    async def authenticate_user(self, login_data: UserLoginSchema) -> User:
        user = await self.user_repo.get_by_username(login_data.username)

        if not user:
            raise ValueError("Invalid username or password")
        
        if not verify_password(user.hashed_password, login_data.password):
            raise ValueError("Invalid password")
        
        return user
