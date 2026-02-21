import asyncpg
from schemas.UserSchema import UserSchema
from services.passwordService import hashPassword


async def setUserCredentials(user: UserSchema, conn: asyncpg.Connection):
    hashedPassword = hashPassword(user.password)

    query = 'INSERT INTO "Users".users(name, age, email, sports, password) VALUES ($1, $2, $3, $4, $5) RETURNING id, name, age, email, sports'

    try:
        return await conn.fetchrow(
            query, user.name, user.age, user.email, user.sports, hashedPassword
        )
    except Exception as e:
        raise e
