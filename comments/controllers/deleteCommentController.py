import asyncpg


async def deleteCommentController(commentid: int, conn: asyncpg.Connection):
    try:
        return await conn.fetchrow(
            'DELETE FROM "Comments".comments where commentid=$1 RETURNING *', commentid
        )
    except Exception as e:
        raise Exception(f"Unable to delete the comment!{e}")
