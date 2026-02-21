import asyncpg


async def deletePostController(id: int, conn: asyncpg.Connection):
    try:
        result = await conn.fetchrow(
            'DELETE FROM "Posts".posts WHERE id=$1 RETURNING id, userid', id
        )

        return result
    except Exception as e:
        raise Exception(f"Unable to delete post!{e}")
