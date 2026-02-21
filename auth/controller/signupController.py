import asyncpg
from schemas.UserSchema import UserSchema
from services.setUserCredentials import setUserCredentials


async def signupController(user: UserSchema, conn: asyncpg.Connection):
    return await setUserCredentials(user=user, conn=conn);
