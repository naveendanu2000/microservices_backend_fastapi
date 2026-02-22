from fastapi import APIRouter, Request
from controllers.deleteCommentController import deleteCommentController

router = APIRouter()


@router.delete("/{commentid}", tags=["Comments"])
async def deleteComment(commentid: int, request: Request):
    pool = request.app.state.pool

    async with pool.acquire() as conn:
        return await deleteCommentController(commentid=commentid, conn=conn)
