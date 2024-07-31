from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from backend.src.s3.router import router as s3_router


main_app = FastAPI()


@main_app.get("/")
async def serve_frontend():
    with open("frontend/index.html") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)


main_app.include_router(s3_router)
