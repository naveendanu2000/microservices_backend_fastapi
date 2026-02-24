import asyncpg
from fastapi import HTTPException
import httpx


async def deletePostController(id: int, userid: int, conn: asyncpg.Connection):
    try:
        result = await conn.fetchrow(
            'DELETE FROM "Posts".posts WHERE id=$1 AND userid=$2 RETURNING id, userid',
            id,
            userid,
        )

        if result:
            res = dict(result)
            try:
                async with httpx.AsyncClient() as client:
                    await client.delete(f"http://localhost:8004/posts/{res['id']}")
            except Exception as e:
                raise Exception(f"Unable to post to event bus! {e}")
            finally:
                return result

        if not result:
            raise HTTPException(
                status_code=401,
                detail="Unauthorized! You may delete post created by you only!",
            )

    except Exception as e:
        raise Exception(f"Unable to delete post!{e}")
