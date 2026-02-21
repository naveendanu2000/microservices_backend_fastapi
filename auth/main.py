from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from contextlib import asynccontextmanager
from routers.signin import router as signinRouter
from connection.connection import create_pool, close_pool


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting the app")

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


@app.get("/")
def home():
    return "Welcome to the Auth service!"
