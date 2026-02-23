from fastapi import FastAPI
from routers.authRouter import router as authRouter
from routers.postRouter import router as postRouter
from routers.commentRouter import router as commentRouter

app = FastAPI()

app.include_router(authRouter)
app.include_router(postRouter)
app.include_router(commentRouter)


@app.get("/")
def home():
    return "Welcome to Posting.com"
