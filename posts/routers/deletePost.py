from fastapi import APIRouter, Request, HTTPException
import httpx
from controllers.deletePostController import deletePostController
from services.verifyJWT import verifyJWT


router = APIRouter()


@router.delete("/posts/{postid}", tags=["Posts"])
async def deletePost(postid: int, request: Request):
    pool = request.app.state.pool

    token = request.cookies.get("access_token")

    userid = verifyJWT(token=token)

    if not userid:
        raise HTTPException(status_code=401, detail="session expired!")

    async with pool.acquire() as conn:
        res = await deletePostController(id=postid, userid=userid, conn=conn)

        if res:
            async with httpx.AsyncClient() as client:
                try:
                    event_res = await client.delete(
                        f"http://localhost:8004/posts/{postid}"
                    )
                except Exception as e:
                    raise Exception(f"Unable to post event to eventbus! {e}")
                finally:
                    return res
