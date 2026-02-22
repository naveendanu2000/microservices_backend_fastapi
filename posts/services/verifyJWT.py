import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import HTTPException
import os

token_expire_minutes = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
jwtSecret = os.getenv("JWT_SECRET")
algorithm = os.getenv("ALGORITHM")


def verifyJWT(token: str | None) -> int:
    if not token:
        raise HTTPException(status_code=401, detail="Unauthorized!")
    if not jwtSecret or not algorithm:
        raise HTTPException(status_code=500, detail="Server configuration error!")
    try:
        payload = jwt.decode(jwt=token, key=jwtSecret, algorithms=[algorithm])

        userid = payload.get("id")

        if userid is None:
            raise Exception("Credentials Exception!")

        return userid

    except InvalidTokenError as e:
        raise HTTPException(status_code=401, detail=f"Invalid Session!{e}")
