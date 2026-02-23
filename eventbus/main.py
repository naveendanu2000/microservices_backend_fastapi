from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from connection.connection import create_pool, close_pool

from routers.postCreatedRouter import router as postCreatedRouter
from routers.postDeletedRouter import router as postDeletedRouter
from routers.userCreatedRouter import router as userCreatedRouter
from routers.userDeletedRouter import router as userDeletedRouter


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Staring the eventbus")
    try:
        await create_pool(app=app)
        print("Connected to DB!")
    except Exception as e:
        raise Exception(f"Unable to start eventbus{e}")

    try:
        yield
    finally:
        print("Closing the app")
        try:
            await close_pool(app=app)
            print("Disconnectd from DB!")
        except Exception as e:
            raise Exception(f"Unable to disconnect the DB! {e}")


app = FastAPI(lifespan=lifespan)

app.include_router(userCreatedRouter)
app.include_router(userDeletedRouter)
app.include_router(postCreatedRouter)
app.include_router(postDeletedRouter)


@app.get("/")
def home():
    return "welcome to the event bus"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8004)
