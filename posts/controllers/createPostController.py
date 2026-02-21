import asyncpg
from schemas.PostSchema import PostSchema


async def createPostController(post: PostSchema, conn: asyncpg.Connection):
    try:
        result = await conn.fetchrow(
            'INSERT INTO "Posts".posts(userid, content) VALUES ($1, $2) RETURNING id, userid, content',
            post.userid,
            post.content,
        )
        return result

    except Exception as e:
        return e
