from fastapi import APIRouter, Request
from services.gateway import forward_request, COMMENTS_SERVICE

router = APIRouter()


@router.api_route(
    "/comments", methods=["GET", "POST", "PUT", "DELETE", "PATCH"], tags=["Comments"]
)
@router.api_route(
    "/comments/{path:path}",
    methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    tags=["Comments"],
)
async def comments_proxy(request: Request, path: str = ""):
    if path:
        target_url = f"{COMMENTS_SERVICE}/{path}"
    else:
        target_url = f"{COMMENTS_SERVICE}"
    return await forward_request(request, target_url)
