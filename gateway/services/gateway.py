from fastapi import FastAPI, Request, Response
import httpx

app = FastAPI()

AUTH_SERVICE = "http://localhost:8001"
POSTS_SERVICE = "http://localhost:8002"


async def forward_request(request: Request, target_url: str):
    async with httpx.AsyncClient() as client:
        resp = await client.request(
            method=request.method,
            url=target_url,
            headers=request.headers,
            content=await request.body(),
            params=request.query_params,
        )

    return Response(
        content=resp.content,
        status_code=resp.status_code,
        headers=dict(resp.headers),
    )