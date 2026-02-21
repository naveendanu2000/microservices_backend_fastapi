from typing import List
from schemas.UserCredentialsSchema import UserCredentials
import asyncpg


async def getUserCredentials(user: UserCredentials, conn: asyncpg.Connection) -> List[dict]:
    rows: List[asyncpg.Record] = await conn.fetch(
        f"SELECT * from \"Users\".users WHERE name='{user.username}'"
    )
    return [dict(row) for row in rows]
