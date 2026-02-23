from fastapi import APIRouter, Request
from controllers.deleteUserController import deleteUserController

router = APIRouter()


@router.delete("/users/{userid}", tags=["Connections"])
async def deleteUser(userid: int, request: Request):
    pool = request.app.state.pool

    async with pool.acquire() as conn:
        await deleteUserController(userid=userid, conn=conn)
