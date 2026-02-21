import jwt
import os
from datetime import datetime, timedelta, timezone

token_expire_minutes = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
jwtSecret = os.getenv("JWT_SECRET")
algorithm = os.getenv("ALGORITHM")


def generateJWT(data: str):
    expire = datetime.now(timezone.utc) + timedelta(minutes=int(token_expire_minutes))

    payload = {
        "sub": data,
        "exp": expire,
    }

    encoded_jwt = jwt.encode(payload=payload, key=jwtSecret, algorithm=algorithm)

    return encoded_jwt
