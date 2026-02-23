import asyncpg
from schemas.UserSchema import UserSchema
import httpx
from urls.urls import POSTS_USER, COMMENTS_USER


async def userCreatedController(user: UserSchema, conn: asyncpg.Connection):
    try:
        async with httpx.AsyncClient() as client:
            posts_response = await client.post(POSTS_USER, data=user.model_dump())
            comments_response = await client.post(COMMENTS_USER, data=user.model_dump())

            response = await conn.fetchrow(
                'INSERT INTO "Events".user_events(event_type, posts_updated, comments_updated)	VALUES ($1, $2, $3)',
                "c",
                posts_response.is_success,
                comments_response.is_success,
            )

            return response
    except Exception as e:
        raise Exception(f"Unable to save data! {e}")
