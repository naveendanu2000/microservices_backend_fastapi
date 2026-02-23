from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from contextlib import asynccontextmanager
from connection.connection import create_pool, close_pool
import uvicorn

from routers.getPosts import router as getAllPostsRouter
from routers.getPostById import router as getPostById
from routers.createPosts import router as createPostsRouter
from routers.deletePost import router as deletePostsRouter
from routers.createUser import router as createUserRouter
from routers.deleteUser import router as deleteUserRouter


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting the posts service")
    try:
        await create_pool(app=app)
        print("Connected to DB!")
    except Exception as e:
        print(f"Unable to connect to DB!{e}")
        raise

    try:
        yield
    finally:
        print("Closing the app")
        try:
            await close_pool(app=app)
            print("Disconnected from the DB!")
        except Exception as e:
            print(f"Unable to connect to DB!{e}")


app = FastAPI(lifespan=lifespan)


app.include_router(getAllPostsRouter)
app.include_router(getPostById)
app.include_router(createPostsRouter)
app.include_router(deletePostsRouter)
app.include_router(createUserRouter)
app.include_router(deleteUserRouter)


@app.get("/")
def home():
    return "Welcome to the Posts service!"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8002)
