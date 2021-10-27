from fastapi import FastAPI

from .routers import dggsZQQuery, dggsZQSet

app = FastAPI()
app.include_router(dggsZQSet.router)
app.include_router(dggsZQQuery.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
