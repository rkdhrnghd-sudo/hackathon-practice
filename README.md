# hackathon-practice

Pre-SKALA 해커톤 연습용 FastAPI 앱.
Python 3.10 이상에서 동작한다.

## API

- `GET /` : 인사 메시지
- `GET /health` : 상태 확인
- `GET /hello` : 이름을 적으면 인사해 주는 화면
- `GET /api/hello?name=이름` : 인사말

## 실행 방법

`uvicorn app.main:app --reload`
