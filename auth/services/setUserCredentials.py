import asyncpg
import httpx
from schemas.UserSchema import UserSchema
from services.passwordService import hashPassword


async def setUserCredentials(user: UserSchema, conn: asyncpg.Connection):
    hashedPassword = hashPassword(user.password)

    query = 'INSERT INTO "Users".users(name, age, email, sports, password) VALUES ($1, $2, $3, $4, $5) RETURNING id, name, age, email, sports'

    try:
        res = await conn.fetchrow(
            query, user.name, user.age, user.email, user.sports, hashedPassword
        )

        if res:
            res_dict = dict(res)
            print("dict data", res_dict["id"], res_dict["name"])
            try:
                print("Posting to eventbus")
                async with httpx.AsyncClient() as client:
                    result = await client.post(
                        "http://localhost:8004/users",
                        json={"id": int(res_dict["id"]), "username": res_dict["name"]},
                    )
                    print(f"printing the event to event bus {result}")
            except Exception as e:
                raise Exception("Event not posted to eventbus! {e}")
            finally:
                return res
    except Exception as e:
        raise e
