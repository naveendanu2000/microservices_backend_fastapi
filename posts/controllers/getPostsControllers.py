import asyncpg


async def getPostsController(conn: asyncpg.Connection):
    try:
        rows = await conn.fetch('SELECT * FROM "Posts".posts ORDER BY id ASC')

        return [dict(row) for row in rows]
    except Exception as e:
        raise e
