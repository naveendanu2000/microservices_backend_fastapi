from fastapi import APIRouter, Request


router = APIRouter()


@router.delete("/{userid}", tags=["Posts"])
async def deleteUser(userid: int, request: Request):
    pool = request.app.state.pool

    async with pool.acquire() as conn:
        return await deleteUserController(userid=userid, conn=conn)
