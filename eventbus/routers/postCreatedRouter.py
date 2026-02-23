from fastapi import APIRouter, Request
from schemas.UserSchema import UserSchema
from controllers.postCreatedController import postCreatedController

router = APIRouter()


@router.post("/posts", tags=["USER_EVENT"])
async def publishPostCreatedEvent(postid: int, request: Request):
    pool = request.app.state.pool

    async with pool.acquire() as conn:
        return await postCreatedController(postid=postid, conn=conn)
