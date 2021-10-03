from fastapi import FastAPI
from app.api import portfolio_api
from app.db import init_db

app = FastAPI()
#Invoke the routes
app.include_router(portfolio_api.router)

@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/ping", include_in_schema=False)
async def pong():
    return {"ping": "pong!"}