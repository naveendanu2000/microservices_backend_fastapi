import asyncpg


async def deletePostController(postid: int, conn: asyncpg.Connection):
    try:
        result = await conn.fetchrow(
            'DELETE FROM "Connections".posts WHERE id=$1 RETURNING *', postid
        )

        return result
    except Exception as e:
        raise Exception(f"Unable to delete post {e}")
