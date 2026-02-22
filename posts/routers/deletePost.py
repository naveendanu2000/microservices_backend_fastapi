from fastapi import APIRouter, Request, HTTPException
from controllers.deletePostController import deletePostController
from services.verifyJWT import verifyJWT


router = APIRouter()


@router.delete("/delete/{postid}", tags=["Posts"])
async def deletePost(postid: int, request: Request):
    pool = request.app.state.pool

    token = request.cookies.get("access_token")

    userid = verifyJWT(token=token)

    if not userid:
        raise HTTPException(status_code=401, detail="session expired!")

    async with pool.acquire() as conn:
        return await deletePostController(id=postid, userid=userid, conn=conn)
