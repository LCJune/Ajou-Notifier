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

### 핵심 클래스: Response
requests.get() 등을 호출하면 반환되는 결과물이 바로  
**Response** 클래스의 인스턴스이다. 이 객체에 서버가 보낸 모든 정보가 담겨 있다.    
<br/>  

**1. 응답 상태 확인(Status)**  
요청이 성공했는지, 실패했다면 어떤 이유인지 확인하는 기능
> <img width="649" height="185" alt="image" src="https://github.com/user-attachments/assets/124da275-ac47-4b73-abb8-914afed50428" />  
<br/>

**2. 본문 데이터 읽기(Content)**  
서버에서 가져온 실제 데이터를 추출하는 기능
> <img width="564" height="183" alt="image" src="https://github.com/user-attachments/assets/a7c76e5b-f85f-4554-9632-5d7de4c7a470" />
<br/>

**3. 메타데이터 및 헤더(Metadata & Header)**  
응답 본문 외의 부가적인 정보들을 확인하는 기능
> <img width="549" height="190" alt="image" src="https://github.com/user-attachments/assets/5ac680f8-6fef-4876-93ab-6129440235b4" />
<br/>

**4. 기록 및 추적(History)**
통신 과정에서 발생한 시간이나 경로를 확인하는 기능
> <img width="626" height="147" alt="image" src="https://github.com/user-attachments/assets/73337747-e30c-4da7-ac97-3eb0a27e8da2" />

### 핵심 클래스: Session











