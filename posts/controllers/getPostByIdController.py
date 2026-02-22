import asyncpg


async def getPostByIdController(conn: asyncpg.Connection, postid: int):
    try:
        result = await conn.fetchrow('SELECT * FROM "Posts".posts where id=$1', postid)

        return result
    except Exception as e:
        raise e
