from fastapi import APIRouter, Request, HTTPException
from schemas.PostSchema import PostSchema
from controllers.createPostController import createPostController
from services.verifyJWT import verifyJWT

router = APIRouter()


@router.post("/posts", tags=["Posts"])
async def createPost(post: PostSchema, request: Request):
    pool = request.app.state.pool

    token = request.cookies.get("access_token")

    userid = verifyJWT(token)

    if not userid:
        raise HTTPException(status_code=401, detail="session expired!")

    async with pool.acquire() as conn:
        return await createPostController(post, conn)
