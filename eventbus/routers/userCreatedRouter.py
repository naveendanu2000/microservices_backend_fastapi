from fastapi import APIRouter, Request
from schemas.UserSchema import UserSchema
from controllers.userCreatedController import userCreatedController

router = APIRouter()


@router.post("/users", tags=["USER_EVENT"])
async def publishUserCreatedEvent(user: UserSchema, request: Request):
    pool = request.app.state.pool

    async with pool.acquire() as conn:
        return await userCreatedController(user=user, conn=conn)
