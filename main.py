import time

from fastapi.websockets import WebSocket

from templates import templates

from fastapi import FastAPI, HTTPException
from fastapi import Request
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse

from db import models
from db.database import engine
from exceptions import StoryException
from auth import authentication
from router import blog_get, user, user_article, product, blog_post, file
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from chat_client import html

app = FastAPI()
app.include_router(templates.router)
app.include_router(authentication.router)
app.include_router(file.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(user_article.router)
app.include_router(product.router)


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={'detail': exc.name}
    )
# @app.get("/")
# async def get():
#     return HTMLResponse(html)
#
# clients=[]
#
# @app.websocket("/chat")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     clients.append(websocket)
#     while True:
#         data = await websocket.receive_text()
#         for client in clients:
#             await client.send_text(data)

# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: HTTPException) -> PlainTextResponse:
#     return PlainTextResponse(str(exc), status_code=400)


models.Base.metadata.create_all(engine)

@app.middleware("http")
async def add_middleware(request: Request, call_next):
    start_time=time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    response.headers["duration"] = str(duration)
    return response

origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.mount("/files", StaticFiles(directory="files"), name="files")
app.mount("/templates/static", StaticFiles(directory="templates/static"), name="static")