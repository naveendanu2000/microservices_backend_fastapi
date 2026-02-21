from fastapi import APIRouter, Request
from controllers.getPostsControllers import getPostsController

router = APIRouter()


@router.get("/all", tags=["Posts"])
async def getPosts(request: Request):
    pool = request.app.state.pool

    async with pool.acquire() as conn:
        return await getPostsController(conn=conn)
