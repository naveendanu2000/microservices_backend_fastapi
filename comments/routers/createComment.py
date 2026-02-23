from fastapi import APIRouter, Request
from schemas.CommentSchema import CommentSchema
from controllers.createCommentController import createCommentController


router = APIRouter()


@router.post("/", tags=["Comments"])
async def createComment(comment: CommentSchema, request: Request):
    pool = request.app.state.pool

    async with pool.acquire() as conn:
        return await createCommentController(comment=comment, conn=conn)
