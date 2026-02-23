from fastapi import APIRouter, Request
from controllers.getCommentsController import getCommentsController

router = APIRouter()


@router.get("/{postid}", tags=["Comments"])
async def getComments(postid: int, request: Request):
    pool = request.app.state.pool

    async with pool.acquire() as conn:
        return await getCommentsController(postid=postid, conn=conn)
