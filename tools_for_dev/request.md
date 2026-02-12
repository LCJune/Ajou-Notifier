## request
```python
import request
```
Python에서 HTTP 요청을 보내기 위해 가장 널리 쓰이는 라이브러리이다.
requests는 모듈 전체를 의미하며, 그 안에 핵심적인 역할을 하는 Response 클래스와 Session 클래스 등이 포함되어 있다.  
<br/> 

### 주요 메서드
* requests.get(url): 데이터 조회
* requests.post(url, data=...): 데이터 생성/전송
* requests.put(url, data=...): 데이터 수정
* requests.delete(url): 데이터 삭제
<br />

### 핵심 클래스: Response 객체
requests.get() 등을 호출하면 반환되는 결과물이 바로
**Response** 클래스의 인스턴스이다. 이 객체에 서버가 보낸 모든 정보가 담겨 있다.    
> <img width="649" height="185" alt="image" src="https://github.com/user-attachments/assets/124da275-ac47-4b73-abb8-914afed50428" />  








