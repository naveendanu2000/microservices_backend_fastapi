import asyncpg
from schemas.CommentSchema import CommentSchema


async def createCommentController(comment: CommentSchema, conn: asyncpg.Connection):
    try:
        return await conn.fetchrow(
            'INSERT INTO "Comments".comments(content, userid, postid) VALUES ($1, $2, $3) RETURNING *',
            comment.content,
            comment.userid,
            comment.postid,
        )

    except Exception as e:
        raise Exception(f"Unable to save the DATA!{e}")
