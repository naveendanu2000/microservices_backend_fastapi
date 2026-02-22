import asyncpg
from fastapi import HTTPException


async def deleteCommentController(
    commentid: int, userid: int, conn: asyncpg.Connection
):
    try:
        result = await conn.fetchrow(
            'DELETE FROM "Comments".comments where commentid=$1 AND userid=$2 RETURNING *',
            commentid,
            userid,
        )

        if not result:
            raise HTTPException(
                status_code=401,
                detail="Unauthorized! You may delete the comments create by you.",
            )
        return result
    except Exception as e:
        raise Exception(f"Unable to delete the comment!{e}")
