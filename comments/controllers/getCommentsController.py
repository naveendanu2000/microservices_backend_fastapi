import asyncpg


async def getCommentsController(postid: int, conn: asyncpg.Connection):
    try:
        result = await conn.fetch(
            'SELECT * FROM "Comments".comments WHERE postid=$1', postid
        )
        return [dict(row) for row in result]
    except Exception as e:
        raise Exception(f"Unable to fetch data{e}")
