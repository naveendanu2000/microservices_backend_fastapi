from fastapi import APIRouter, Request
from services.gateway import forward_request, AUTH_SERVICE

router = APIRouter()


@router.api_route("/auth/{path:path}", methods=["GET", "POST"], tags=["Auth"])
async def auth_proxy(path: str | None, request: Request):
    if path:
        target_url = f"{AUTH_SERVICE}/{path}"
    else:
        target_url = f"{AUTH_SERVICE}"
    return await forward_request(request, target_url)
