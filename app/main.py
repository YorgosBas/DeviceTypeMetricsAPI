from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import create_tables, engine

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables(engine) 
    yield

app.lifespan = lifespan

from app.api.api_v1.router import api_router
app.include_router(api_router)