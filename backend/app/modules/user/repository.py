from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from typing import Dict, Any
from .model import User

# In my repository class there is no error handling 
# because according to the MVC architecture pattern
# the repository should be “dumb” and this should be the role of the service layer.

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    # ------------------------------------- CREATE ----------------------------------------------------------------------

    async def create_user(self, user_data: dict) -> User:
        user = User(**user_data)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
    
    # ---------------------------------------- READ ----------------------------------------------------------------------

    async def list_all_users(self, skip: int = 0, limit: int = 10):
        query = select(User).offset(skip).limit(limit)

        result = await self.session.execute(query)

        return result.scalars().all()

# This is a function designed exclusively to assist the output of list_all_users. It may be removed from this code soon.

    async def users_count(self) -> int:
        query = select(User)

        result = await self.session.execute(query)

        return len(result.scalars().all())

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
    
    # ---------------------------------------- UPDATE -----------------------------------------------------------

    async def patch_method(self, id: int, user_update_data: Dict[str, Any]) -> User | None:
        query = (
            update(User)
            .where(User.id == id)
            .values(**user_update_data)
            .returning(User)
        )

        result = await self.session.execute(query)
        updated_user = result.scalars().first()
        await self.session.commit()

        return updated_user
    
    # -------------------------------------- DELETE ----------------------------------------------------------------------

    async def delete_by_id(self, user: User) -> None:
        await self.session.delete(user)
        await self.session.commit()
    