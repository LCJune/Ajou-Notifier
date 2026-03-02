## BeautifulSoup
```python
from bs4 import BeautifulSoup
```
파이썬에서 **XML**이나 **HTML** 데이터를 추출하기 위해 사용하는 라이브러리.  
find(), select(), get() 등 직관적인 메서드로 문서 내 요소들을 선택할 수 있다.  
다양한 파서(parser)를 지원해, xml, html5lib 등 다양한 해석 엔진을 선택해 속도나 정확도를 높일 수 있다.  
BeautifulSoup은 트리 구조로 이루어진 웹 브라우저 문서를 분석해 재구성하여 가져온다.   
태그 이름(tag), 속성(id, class) 등을 이용해 원하는 데이터를 뽑아낼 수 있다.  
<br />  

**사용 예시**  
```python
# BeautifulSoup 객체 생성
soup = BeautifulSoup(html_doc, 'html.parser')

# h1 태그의 텍스트 가져오기
print(soup.find('h1').text) # 매개변수를 지정하지 않을 경우, 일반적으로 tag 요소를 가져온다.
# 출력: 오늘의 날씨

# 클래스가 'content'인 p 태그 가져오기
print(soup.find('p', class_='content').text) # class를 탐색하고 싶다면, class_ 매개변수를 지정해야 한다.
```
<br />  

### 주요 메서드
> <img width="796" height="273" alt="image" src="https://github.com/user-attachments/assets/4e23ba4c-4361-4a02-bf47-b9e90a590ea2" />
<br />


### bs4 객체
BeautifulSoup를 이용해 HTML 등의 문서를 파싱하면, 해당 문서는 여러 객체(Object)들의 가계도(트리)로 재구성 된다.  
그리고 그 결과는 bs4의 하위 객체로 반횐되는데, bs4의 핵심 구성 객체는 다음과 같다.  
> <img width="700" height="261" alt="image" src="https://github.com/user-attachments/assets/3a70b847-c493-4ac8-a574-66b82ddd2b4c" />

위 사진에 나온 객체는 모두 **bs4.element** 객체에 포함돼 있다. BeautifulSoup의 메서드를 이용했을 때 반환되는 객체는 모두
<br/>

