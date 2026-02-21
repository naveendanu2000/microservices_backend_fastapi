from fastapi import APIRouter, Request
from services.gateway import forward_request, POSTS_SERVICE

router = APIRouter()


@router.api_route("/posts", methods=["GET", "POST", "PUT", "DELETE"], tags=["Posts"])
@router.api_route(
    "/posts/{path:path}", methods=["GET", "POST", "PUT", "DELETE"], tags=["Posts"]
)
async def posts_proxy(request: Request, path: str = ""):
    if path:
        target_url = f"{POSTS_SERVICE}/{path}"
    else:
        target_url = f"{POSTS_SERVICE}"
    return await forward_request(request, target_url)
