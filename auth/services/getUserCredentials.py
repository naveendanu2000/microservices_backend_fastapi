from schemas.UserCredentialsSchema import UserCredentials


async def getUserCredentials(user: UserCredentials, conn):
    rows = await conn.fetch(
        f"SELECT * from \"Users\".users WHERE name='{user.username}'"
    )
    return [dict(row) for row in rows]
