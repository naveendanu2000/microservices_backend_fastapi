import asyncpg


async def deleteUserController(userid: int, conn: asyncpg.Connection):
    try:
        result = await conn.fetchrow(
            'DELETE FROM "Connections".connections WHERE id=$1 RETURNING *', userid
        )

        return result

    except Exception as e:
        raise Exception(f"Unable to delete user {e}")
