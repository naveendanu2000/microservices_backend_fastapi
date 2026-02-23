import asyncpg
from schemas.UserSchema import UserSchema
import httpx
from urls.urls import COMMENTS_POST


async def postCreatedController(postid: int, conn: asyncpg.Connection):
    try:
        async with httpx.AsyncClient() as client:
            comments_response = await client.post(
                COMMENTS_POST, data={"postid": postid}
            )

            response = await conn.fetchrow(
                'INSERT INTO "Events".posts_events(event_type, comments_updated) VALUES ($1, $2)',
                'c',
                comments_response.is_success,
            )

            return response
    except Exception as e:
        raise Exception(f"Unable to save data! {e}")
