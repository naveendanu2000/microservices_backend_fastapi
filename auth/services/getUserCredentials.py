from schemas.UserCredentialsSchema import UserCredentials
from schemas.UserSchema import UserSchema
import asyncpg


async def getUserCredentials(
    user: UserCredentials, conn: asyncpg.Connection
) -> UserSchema | None:
    row: asyncpg.Record | None = await conn.fetchrow(
        f'SELECT id, name, age, email, sports, password  from "Users".users WHERE name=$1',
        user.username,
    )

    if row is None:
        return None
    else:
        return UserSchema(**row)
