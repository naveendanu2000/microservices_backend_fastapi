from dotenv import load_dotenv

load_dotenv()

import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from connection.connection import create_pool, close_pool


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
            print("Diconnected from the DB!")
        except Exception as e:
            raise Exception(f"Unable to close the DB!{e}")


app = FastAPI()


@app.get("/")
def home():
    return "Welcome to comments service!"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8003)
