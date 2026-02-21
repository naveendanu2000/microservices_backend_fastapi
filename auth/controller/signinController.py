from services.getUserCredentials import getUserCredentials
from schemas.UserCredentialsSchema import UserCredentials


async def signinController(user: UserCredentials, conn):
    # print(user)
    return await getUserCredentials(user=user, conn=conn)
