import asyncpg
from services.getCurrentUser import getCurrentUser
from fastapi import HTTPException


async def getUserController(conn: asyncpg.Connection, token: str):
    username = getCurrentUser(token=token)

    try:
        result: asyncpg.Record | None = await conn.fetchrow(
            'SELECT id, name, email, sports, age FROM "Users".users WHERE name=$1',
            username,
        )
        if not result:
            raise HTTPException(status_code=401, detail="No user found!")
        return dict(**result)
    except Exception as e:
        raise e
