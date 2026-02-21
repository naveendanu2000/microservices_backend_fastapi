from fastapi import APIRouter, Request, HTTPException
from controllers.deletePostController import deletePostController
from services.verifyJWT import verifyJWT


router = APIRouter()


@router.delete("/delete/{id}", tags=["Posts"])
async def deletePost(id: int, request: Request):
    pool = request.app.state.pool

    token = request.cookies.get("access_token")

    username = verifyJWT(token=token)

    if not username:
        raise HTTPException(status_code=401, detail="session expired!")

    async with pool.acquire() as conn:
        return await deletePostController(id=id, conn=conn)
