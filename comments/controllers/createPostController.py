import asyncpg


async def createPostController(postid: int, conn: asyncpg.Connection):
    try:
        result = await conn.fetchrow(
            'INSERT INTO "Comments".posts(id) VALUES ($1) RETURNING *', postid
        )

        return result
    except Exception as e:
        raise Exception(f"Unable to create post {e}")
