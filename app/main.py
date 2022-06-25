import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import task, done

app = FastAPI()
app.include_router(task.router)
app.include_router(done.router)


FRONT_URL = os.environ.get("FRONT_URL")
origins = [FRONT_URL]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
