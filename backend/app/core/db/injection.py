from collections.abc import AsyncGenerator
from .database import asession

async def get_db_session() -> AsyncGenerator:
    async with asession() as session:
        yield session