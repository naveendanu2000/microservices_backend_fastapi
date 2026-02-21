import asyncpg
from services.getUserCredentials import getUserCredentials
from schemas.UserCredentialsSchema import UserCredentials
from schemas.UserSchema import UserSchema
from services.passwordService import verifyPassword
from services.createJWT import generateJWT
from fastapi import HTTPException, Response


async def signinController(
    user: UserCredentials, conn: asyncpg.Connection, response: Response
):
    # print(user)
    row: UserSchema | None = await getUserCredentials(user=user, conn=conn)

    if row is None:
        verifyPassword(user.password, "abcdaklsdja")
        raise HTTPException(status_code=401, detail="Unauthorized!")

    if not verifyPassword(user.password, row.password):
        raise HTTPException(status_code=401, detail="Unauthorized!")

    jwt = generateJWT(user.username)

    response.set_cookie(
        key="access_token",
        value=jwt,
        httponly=True,
        secure=False,
        samesite="lax",
    )
    login_response = {"detail": "Logged in Successfully"}

    return login_response
