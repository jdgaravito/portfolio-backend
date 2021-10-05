from fastapi import FastAPI
from app.api import portfolio_api

app = FastAPI()
#Invoke the routes
app.include_router(portfolio_api.router)



@app.get("/ping", include_in_schema=False)
async def pong():
    return {"ping": "pong!"}