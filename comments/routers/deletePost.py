from fastapi import APIRouter, Request
from controllers.deletePostController import deletePostController


router = APIRouter()


@router.delete("/posts/{postid}", tags=["Posts"])
async def deletePost(postid: int, request: Request):
    pool = request.app.state.pool

    async with pool.acquire() as conn:
        return await deletePostController(postid=postid, conn=conn)
