from fastapi import APIRouter, Request
from controllers.getPostByIdController import getPostByIdController

router = APIRouter()


@router.get("/{postid}", tags=["Posts"])
async def getPosts(postid: int, request: Request):
    pool = request.app.state.pool

    async with pool.acquire() as conn:
        return await getPostByIdController(conn=conn, postid=postid)
