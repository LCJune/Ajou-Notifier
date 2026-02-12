## request
```python
import request
```
Python에서 HTTP 요청을 보내기 위해 가장 널리 쓰이는 라이브러리이다.
requests는 모듈 전체를 의미하며, 그 안에 핵심적인 역할을 하는 Response 클래스와 Session 클래스 등이 포함되어 있다.  
### 주요 메서드
* requests.get(url): 데이터 조회
* requests.post(url, data=...): 데이터 생성/전송
* requests.put(url, data=...): 데이터 수정
* requests.delete(url): 데이터 삭제

### 핵심 클래스: Response 객체
