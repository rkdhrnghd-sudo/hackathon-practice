from pathlib import Path

from fastapi import FastAPI, Query
from fastapi.responses import FileResponse

app = FastAPI()
HELLO_PAGE = Path(__file__).parent / "templates" / "hello.html"


@app.get("/")
def root():
    return {"message": "hello hackathon"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/hello")
def hello_page():
    return FileResponse(HELLO_PAGE)


@app.get("/api/hello")
def hello(name: str = Query(min_length=1, max_length=30)):
    return {"message": f"{name}님, 안녕하세요!"}
