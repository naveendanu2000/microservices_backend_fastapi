import asyncpg
import httpx
from urls.urls import POSTS_USER, COMMENTS_USER


async def userDeletedController(userid: int, conn: asyncpg.Connection):
    try:
        async with httpx.AsyncClient() as client:
            posts_response = await client.post(f"{POSTS_USER}/{userid}")
            comments_response = await client.delete(f"{COMMENTS_USER}/{userid}")

            response = await conn.fetchrow(
                'INSERT INTO "Events".user_events(event_type, posts_updated, comments_updated)	VALUES ($1, $2, $3)',
                'd',
                posts_response.is_success,
                comments_response.is_success,
            )

            return response
    except Exception as e:
        raise Exception(f"Unable to save data! {e}")
