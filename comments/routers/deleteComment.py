from fastapi import APIRouter, Request
from controllers.deleteCommentController import deleteCommentController
from services.verifyJWT import verifyJWT

router = APIRouter()


@router.delete("/{commentid}", tags=["Comments"])
async def deleteComment(commentid: int, request: Request):
    pool = request.app.state.pool

    token = request.cookies.get("access_token")
    userid = verifyJWT(token=token)

    async with pool.acquire() as conn:
        return await deleteCommentController(
            commentid=commentid, userid=userid, conn=conn
        )
