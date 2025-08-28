import asyncio
from logging.config import fileConfig
from pathlib import Path
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from alembic import context
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    raise RuntimeError("DATABASE_URL não encontrado no .env")

config = context.config

alembic_config_file = config.config_file_name
if alembic_config_file is not None:
    fileConfig(Path(alembic_config_file))  

from app.modules.user.model import Base, User

target_metadata = Base.metadata

engine: AsyncEngine = create_async_engine(DATABASE_URL, poolclass=pool.NullPool)

def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online():
    async with engine.connect() as connection:
        await connection.run_sync(do_run_migrations)

if context.is_offline_mode():
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True
    )
    with context.begin_transaction():
        context.run_migrations()
else:
    asyncio.run(run_migrations_online())
