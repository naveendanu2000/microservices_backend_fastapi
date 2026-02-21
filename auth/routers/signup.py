from fastapi import APIRouter, Request
from schemas.UserSchema import UserSchema
from controller.signupController import signupController

router = APIRouter()


@router.post("/signup", tags=["Auth"])
async def signup(user: UserSchema, request: Request):
    pool = request.app.state.pool

    async with pool.acquire() as conn:
        return await signupController(user=user, conn=conn)
