import asyncpg


async def deleteUserController(userid: int, conn: asyncpg.Connection):
    try:
        result = await conn.fetchrow('DELETE FROM "POSTS".users WHERE id=$1', userid)

        return result
    except Exception as e:
        raise Exception(f"Unable to delete User {e}")
