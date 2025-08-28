from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from .model import User

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create_user(self, user_data: dict) -> User:
        user =  User(**user_data)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
    
    async def get_by_username(self, username: str) -> User | None:
        result = await self.session.execute(
            select(User).where(User.username == username)
        )

        return result.scalars().first()
    
    async def get_by_email(self, email: str) -> User | None: 
        result = await self.session.execute(
            select(User).where(User.email == email)
        )

        return result.scalars().first() 
    
    async def get_by_id(self, id: int) -> User | None: 
        result = await self.session.execute(
            select(User).where(User.id == id)
        )

        return result.scalars().first() 
    
    async def delete_by_id(self, user: User) -> None:
        await self.session.delete(user)
        await self.session.commit()
