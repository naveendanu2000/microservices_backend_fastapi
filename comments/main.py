from dotenv import load_dotenv

load_dotenv()

import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from connection.connection import create_pool, close_pool
from routers.createComment import router as createCommentRouter
from routers.deleteComment import router as deleteCommentRouter
from routers.getComments import router as getCommentsRouter
from routers.createUser import router as createUserRouter
from routers.deleteUser import router as deleteUserRouter
from routers.createPost import router as createPostRouter
from routers.deletePost import router as deletePostRouter


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting the comments service")

    try:
        await create_pool(app=app)
        print("Connected to DB!")
    except Exception as e:
        raise Exception(f"Unable to connect to DB! {e}")

    try:
        yield
    finally:
        print("Closing the comments service")
        try:
            await close_pool(app=app)
            print("Diconnected from the DB!")
        except Exception as e:
            raise Exception(f"Unable to close the DB!{e}")


app = FastAPI()

app.include_router(createCommentRouter)
app.include_router(deleteCommentRouter)
app.include_router(getCommentsRouter)
app.include_router(createUserRouter)
app.include_router(deleteUserRouter)
app.include_router(createPostRouter)
app.include_router(deletePostRouter)


@app.get("/")
def home():
    return "Welcome to comments service!"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8003)
