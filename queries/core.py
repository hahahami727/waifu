from sqlalchemy import text, insert
from src.database import sync_engine, async_engine
from src.models import metadata_obj, employers_table

def get_123_sync():
    with sync_engine.connect() as conn:
        result = conn.execute(text("SELECT 1, 2, 3"))
        print(f"{result.first()=}")

async def get_123_async():
    async with async_engine.connect() as conn:
        result = await conn.execute(text("SELECT 1, 2, 3"))
        print(f"{result.first()=}")

def create_tables():
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)
    sync_engine.echo = True

def insert_data():
    with sync_engine.connect() as conn:
        # stmt = """INSERT INTO employers (name) VALUES ('Alice'), 
        # ('Bob'), 
        # ('Charlie');"""
        stmt = insert(employers_table).values([
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
            {"name": "Charlie", "age": 35},
        ])
        conn.execute(stmt)
        conn.commit()      