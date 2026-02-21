from services.getUserCredentials import getUserCredentials
from schemas.UserCredentialsSchema import UserCredentials
import asyncpg


async def signinController(user: UserCredentials, conn: asyncpg.Connection):
    # print(user)
    return await getUserCredentials(user=user, conn=conn)
