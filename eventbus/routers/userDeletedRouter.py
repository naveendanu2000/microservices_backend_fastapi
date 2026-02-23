from fastapi import APIRouter, Request
from schemas.UserSchema import UserSchema
from controllers.userDeletedController import userDeletedController

router = APIRouter()


@router.delete("/users/{userid}", tags=["USER_EVENT"])
async def publishUserDeletedEvent(userid: int, request: Request):
    pool = request.app.state.pool

    async with pool.acquire() as conn:
        return await userDeletedController(userid=userid, conn=conn)
