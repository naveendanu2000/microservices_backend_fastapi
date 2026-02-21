from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from contextlib import asynccontextmanager
from connection.connection import create_pool, close_pool
import uvicorn

from routers.signin import router as signinRouter
from routers.signup import router as signupRouter
from routers.getUser import router as getUserRouter


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting the auth service")

    try:
        await create_pool(app=app)
        print("Connected to DB!")
    except Exception as e:
        print(f"Unable to connect to DB! {e}")
        raise

    try:
        yield
    finally:
        print("Closing the app")
        try:
            await close_pool(app=app)
            print("Disconnected from the DB!")
        except Exception as e:
            print(f"Unable to connect to DB! {e}")


app = FastAPI(lifespan=lifespan)


app.include_router(signinRouter)
app.include_router(signupRouter)
app.include_router(getUserRouter)


@app.get("/")
def home():
    return "Welcome to the Auth service!"

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8001)