from fastapi import APIRouter, Request
from controllers.createPostController import createPostController


router = APIRouter()


@router.post("/posts", tags=["Posts"])
async def createPost(postid: int, request: Request):
    pool = request.app.state.pool

    async with pool.acquire() as conn:
        return await createPostController(postid=postid, conn=conn)
