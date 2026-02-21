from fastapi import APIRouter, Request
from schemas.UserCredentialsSchema import UserCredentials
from controller.signinController import signinController

router = APIRouter()


@router.post("/auth/signin", tags=["Auth"])
async def signin(user: UserCredentials, request: Request):
    pool = request.app.state.pool
    # print(user)
    async with pool.acquire() as conn:
        return await signinController(user=user, conn=conn)
