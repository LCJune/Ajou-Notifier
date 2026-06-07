## HTTPAdatper
Adapter 객체는 실제 통신 요청을 보내는 주체로서, requests 객체의 요청을 받아 urlib3에 통신 요청을 보낸다.  
HTTP, HTTPS, SOCKS Proxy, Custom Protocol 등의 다양한 프로토콜에 맞는 Adapter 클래스가 존재한다.    
Adapter 객체는 Retry와 같은 통신 정책에 대한 정보를 가진 객체를 담을 수 있다.  
각 Adapter는 requests 객체의 mount() 메서드를 통해, 특정 URL 형식의 통신에 배정된다.

### Retry
통신 실패 시 재시도 정책에 대한 정보를 담는 객체이다.
생성자의 argument는,  
total : 재시도 횟수  
backoff_factor : 재시도 간격
status_forcelist: list 내의 상태 코드에서만 재시도  
<br />  
등이 있다.
