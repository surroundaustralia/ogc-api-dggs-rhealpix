from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from .routers import dggsZQQuery, dggsZQSet

app = FastAPI()
app.include_router(dggsZQSet.router)
app.include_router(dggsZQQuery.router)


@app.get("/", response_class=HTMLResponse)
async def root():
    html_content = Path("app/static/home.html").read_text()
    return HTMLResponse(content=html_content, status_code=200)
