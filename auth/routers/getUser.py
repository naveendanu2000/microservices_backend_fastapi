from fastapi import APIRouter, Request, HTTPException
from controller.getUserController import getUserController

router = APIRouter()


@router.get("/user", tags=["Auth"])
async def getUser(request: Request):
    pool = request.app.state.pool
    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(status_code=401, detail="Session ended please login in!")

    async with pool.acquire() as conn:
        user = await getUserController(conn=conn, token=token)

        if not user:
            raise HTTPException(status_code=401, detail="Session Timed out!")

        return user
