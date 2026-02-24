import asyncpg
from schemas.PostSchema import PostSchema
import httpx


async def createPostController(post: PostSchema, conn: asyncpg.Connection):
    try:
        result = await conn.fetchrow(
            'INSERT INTO "Posts".posts(userid, content) VALUES ($1, $2) RETURNING id, userid, content',
            post.userid,
            post.content,
        )

        if result:
            try:
                res = dict(result)
                async with httpx.AsyncClient() as client:
                    await client.post(
                        "http://localhost:8004/posts", json={"postid": res["id"]}
                    )
            except Exception as e:
                raise Exception(f"Unable to post event to Event bus! {e}")
            finally:
                return result

    except Exception as e:
        return e
