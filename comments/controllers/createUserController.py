import asyncpg
from schemas.UserSchema import UserSchema


async def createUserController(user: UserSchema, conn: asyncpg.Connection):
    try:
        result = await conn.fetchrow(
            'INSERT INTO "Comments".users(id, username) VALUES ($1, $2) RETURNING *',
            user.id,
            user.username,
        )
        return result

    except Exception as e:
        raise Exception(f"Unable to save the data {e}")
