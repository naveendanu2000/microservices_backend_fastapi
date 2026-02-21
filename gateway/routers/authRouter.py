from fastapi import APIRouter, Request
from services.gateway import forward_request, AUTH_SERVICE

router = APIRouter()


@router.api_route("/auth/{path:path}", methods=["GET", "POST", "PUT", "DELETE"], tags=['Auth'])
async def auth_proxy(path: str, request: Request):
    target_url = f"{AUTH_SERVICE}/{path}"
    return await forward_request(request, target_url)
