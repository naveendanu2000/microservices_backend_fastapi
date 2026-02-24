from fastapi import APIRouter, Request
from controllers.postDeletedController import postDeletedController

router = APIRouter()


@router.delete("/posts/{postid}", tags=["POST_EVENT"])
async def publishPostDeletedEvent(postid: int, request: Request):
    pool = request.app.state.pool

    async with pool.acquire() as conn:
        return await postDeletedController(postid=postid, conn=conn)
