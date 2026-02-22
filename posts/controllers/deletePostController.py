import asyncpg
from fastapi import HTTPException


async def deletePostController(id: int, userid: int, conn: asyncpg.Connection):
    try:
        result = await conn.fetchrow(
            'DELETE FROM "Posts".posts WHERE id=$1 AND userid=$2 RETURNING id, userid',
            id,
            userid,
        )

        if not result:
            raise HTTPException(
                status_code=401,
                detail="Unauthorized! You may delete post created by you only!",
            )

        return result
    except Exception as e:
        raise Exception(f"Unable to delete post!{e}")
