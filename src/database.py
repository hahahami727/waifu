from sqlalchemy import URL, create_engine, text
from sqlalchemy.ext import asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker, Session
from config import settings
import asyncio

sync_engine = create_engine(
    url=settings.database_URL_psycopg,
    echo=True,
    # pool_size=5,
    # pool_max_overflow=10,
    )

async_engine = create_async_engine(
    url=settings.database_URL_asyncpg,
    echo=True,
    # pool_size=5,
    # pool_max_overflow=10,
    )


with sync_engine.connect() as conn:
    result = conn.execute(text("SELECT VERSION()"))
    print(f"{result.one()=}")

async def test_async_connection():
    async with async_engine.connect() as conn:
        result = await conn.execute(text("SELECT 1, 2, 3"))
        print(f"{result.one()=}")

asyncio.run(test_async_connection())       