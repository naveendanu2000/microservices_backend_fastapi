from fastapi import APIRouter, Request
from services.gateway import forward_request, POSTS_SERVICE

router = APIRouter()


@router.api_route(
    "/posts/{path:path}", methods=["GET", "POST", "PUT", "DELETE"], tags=["Posts"]
)
async def posts_proxy(path: str, request: Request):
    target_url = f"{POSTS_SERVICE}/{path}"
    return await forward_request(request, target_url)
