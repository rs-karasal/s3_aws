from fastapi import FastAPI
from fastapi.responses import HTMLResponse


main_app = FastAPI()


@main_app.get("/")
async def serve_frontend():
    with open("frontend/index.html") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)
