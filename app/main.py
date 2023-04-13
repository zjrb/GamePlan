import os
from fastapi import FastAPI
from app.routers import offense

app = FastAPI()

app.include_router(offense.offense, prefix="/offense", tags=["offense"])


@app.get("/")
def read_root():
    return {"Hello": "World"}
