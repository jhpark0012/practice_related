from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

# FastAPI 애플리케이션(= 웹 서버 앱) 생성
# 이 app 객체가 "어떤 URL로 요청이 오면 어떤 함수를 실행할지"를 관리한다.
# 쉽게 말해:
# - 브라우저/Postman이 특정 주소로 요청을 보냄
# - FastAPI가 그 주소와 맞는 함수를 찾아 실행함
app = FastAPI(
    # /docs 같은 자동 문서 페이지에 표시되는 API 제목
    title='FastAPI-Hello World code',

    # API 문서에 표시되는 설명
    # 브라우저 첫 화면(/)에 자동으로 뜨는 내용은 아님
    description="This is the Hello World",

    # API 버전 정보
    # 이것도 주로 문서 페이지(/docs)에서 확인하는 메타데이터
    version="1.0.0",
)

# Request Body(요청 본문)로 들어올 JSON 데이터의 구조를 정의
# 주로 POST/PUT 같은 요청에서 클라이언트가 서버로 데이터를 보낼 때 사용한다.
#
# 예를 들어 클라이언트가 이런 JSON을 보내면:
# {
#   "name": "apple",
#   "description": "fresh",
#   "price": 1000,
#   "tax": 100
# }
#
# FastAPI는 이 JSON을 Item 형태로 해석해서 post_test 함수의 item 파라미터에 넣어준다.
#
# 즉, 이 클래스는 "서버가 어떤 형식의 JSON을 받을지"를 정의하는 웹용 데이터 스키마다.
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

# GET 요청 + 루트 URL("/") 처리
#
# 사용 예:
# 브라우저나 Postman에서 아래 주소로 GET 요청을 보내면 이 함수가 실행된다.
# http://127.0.0.1:8000/
#
# 여기서:
# - GET은 "서버에서 데이터 조회/확인"할 때 가장 많이 쓰는 HTTP 메서드
# - "/"는 사이트의 기본 주소(루트 경로)
#
# return 값은 HTTP 응답으로 클라이언트에게 전달된다.
@app.get('/')
def hello_world():
    return "Hello World!"

# GET 요청 + 경로 파라미터(path parameter) 예제
#
# URL 패턴:
# /get_test/{input_val}
#
# 여기서 {input_val}는 URL 경로 일부를 변수처럼 받겠다는 뜻이다.
#
# 예:
# GET /get_test/123
# -> input_val = "123"
#
# 즉, 주소 일부를 잘라서 함수 인자로 넣어주는 방식이다.
# 이런 값은 보통 "리소스 식별자", "id", "카테고리명", "특정 값" 등을 표현할 때 자주 쓴다.
@app.get('/get_test/{input_val}')
def get_test1(input_val):
    # 서버가 JSON 형태의 응답을 반환
    # FastAPI는 dict를 자동으로 JSON으로 바꿔서 응답해준다.
    return {"values": input_val}

# GET 요청 + 경로 파라미터(path parameter) + 쿼리 파라미터(query parameter) 예제
#
# URL 패턴:
# /get_test2/{input_val}
#
# 함수 인자 설명:
# - input_val: 경로(path)에서 받는 값
# - q: 쿼리 문자열(query string)에서 받는 값
#
# 예를 들어 아래 요청이 들어오면:
# GET /get_test2/123?q=hello
#
# FastAPI는 이렇게 해석한다:
# - input_val = 123   (URL 경로에서 추출)
# - q = "hello"       (? 뒤의 query string에서 추출)
#
# URL을 나누어 보면:
# /get_test2/123      -> path 부분
# ?q=hello            -> query parameter 부분
#
# 보통:
# - path parameter는 "무엇을 대상으로 할지" 나타낼 때 많이 쓰고
# - query parameter는 "추가 옵션/필터/검색조건"을 보낼 때 많이 쓴다.
@app.get('/get_test2/{input_val}')
def get_test2(input_val: int, q: str):
    # 응답 JSON 예시:
    # {
    #   "item_id": 123,
    #   "q": "hello"
    # }
    return {"item_id": input_val, "q": q}

# POST 요청 예제
#
# POST는 클라이언트가 서버에 데이터를 "보낼 때" 자주 쓰는 HTTP 메서드다.
# 주로 생성(create), 등록(register), 저장(save) 같은 작업에 사용한다.
#
# 이 API는 Request Body에 JSON을 담아서 보내야 한다.
#
# 요청 예시:
# POST /post_test
# Content-Type: application/json
#
# Body:
# {
#   "name": "apple",
#   "description": "fresh",
#   "price": 1000,
#   "tax": 100
# }
#
# 그러면 FastAPI는 이 JSON을 Item 모델에 맞춰 검증한 뒤,
# item 파라미터에 넣어서 함수에 전달한다.
#
# 만약 JSON 구조가 Item과 맞지 않으면(예: price에 문자열 넣음),
# FastAPI가 자동으로 에러 응답을 반환한다.
@app.post('/post_test')
def post_test(item: Item):
    # 받은 데이터를 그대로 다시 응답으로 반환
    # 실습 목적상 "서버가 JSON을 제대로 받았는지" 확인하는 용도
    return item