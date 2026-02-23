from fastapi import APIRouter, Request
from schemas.UserSchema import UserSchema
from controllers.createUserController import createUserController

router = APIRouter()


@router.post("/users", tags=["Posts"])
async def createUser(user: UserSchema, request: Request):
    pool = request.app.state.pool

    async with pool.acquire() as conn:
        return await createUserController(user=user, conn=conn)
