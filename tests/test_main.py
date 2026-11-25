from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"message": "hello hackathon"}


def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}


def test_hello_page():
    res = client.get("/hello")
    assert res.status_code == 200
    assert "인사 받기" in res.text


def test_hello_message():
    res = client.get("/api/hello", params={"name": "홍길동"})
    assert res.status_code == 200
    assert res.json() == {"message": "홍길동님, 안녕하세요!"}


def test_hello_without_name():
    assert client.get("/api/hello", params={"name": ""}).status_code == 422
