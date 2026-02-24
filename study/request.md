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
**1. session의 핵심 기능**  
> <img width="773" height="453" alt="image" src="https://github.com/user-attachments/assets/d2dd2270-6cdc-4d6a-9cf4-08e83c83d43d" />

**2. 요청 전송 메서드(HTTP verb methods)**  
> <img width="719" height="355" alt="image" src="https://github.com/user-attachments/assets/ce82fa64-3e3e-4501-a074-f89b5054e197" />

**3. 핵심 범용 메서드**  
> <img width="738" height="120" alt="image" src="https://github.com/user-attachments/assets/222624bc-7435-40f3-b3dc-820909b57267" />
> <img width="244" height="243" alt="image" src="https://github.com/user-attachments/assets/b30cda3a-240b-49c9-870c-e21c7fabf7da" />

**4. 세션 설정 관련 메서드**  
> <img width="678" height="168" alt="image" src="https://github.com/user-attachments/assets/58f38369-ca3e-4397-83c0-6331cbae2adb" />

**5. 중요 속성(필드)**    
> <img width="521" height="268" alt="image" src="https://github.com/user-attachments/assets/b3d09207-3c10-4b27-9561-98983553dd48" />

**6. 내부 동작 구조**
Session  
 ├── request()  
 │     └── prepare_request()  
 │     └── send()  
 │            └── HTTPAdapter  
 │                    └── urllib3 connection pool  

 **7. 정리**  
 > <img width="553" height="160" alt="image" src="https://github.com/user-attachments/assets/f1a7334f-e7e6-4f1c-a84a-077f998dc67f" />   

















