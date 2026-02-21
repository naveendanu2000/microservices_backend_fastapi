import asyncpg
from fastapi import FastAPI
import os

DATABASE_URL = os.getenv("DATABASE_URL")


async def create_pool(app: FastAPI):
    app.state.pool = await asyncpg.create_pool(DATABASE_URL)


async def close_pool(app: FastAPI):
    await app.stata.pool.close()
