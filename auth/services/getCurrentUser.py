import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import HTTPException
import os

token_expire_minutes = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
jwtSecret = os.getenv("JWT_SECRET")
algorithm = os.getenv("ALGORITHM")


def getCurrentUser(token: str | None) -> str:
    if not token:
        raise HTTPException(status_code=401, detail="Unauthorized!")
    try:
        payload = jwt.decode(jwt=token, key=jwtSecret, algorithms=algorithm)

        username = payload.get("sub")

        if username is None:
            raise Exception("Credentials Exception!")

        return username

    except InvalidTokenError as e:
        raise HTTPException(status_code=401, detail=f"Invalid Session!{e}")
