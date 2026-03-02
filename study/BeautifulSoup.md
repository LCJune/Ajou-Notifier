# BeautifulSoup
```python
from bs4 import BeautifulSoup
```
파이썬에서 **XML**이나 **HTML** 데이터를 추출하기 위해 사용하는 라이브러리로,  
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

## 주요 메서드
> <img width="796" height="273" alt="image" src="https://github.com/user-attachments/assets/4e23ba4c-4361-4a02-bf47-b9e90a590ea2" />
<br />


## bs4 객체
BeautifulSoup를 이용해 HTML 등의 문서를 파싱하면, 해당 문서는 여러 객체(Object)들의 가계도(트리)로 재구성 된다.  
그리고 그 결과는 bs4의 하위 객체로 반횐되는데, bs4의 핵심 구성 객체는 다음과 같다.  
> <img width="700" height="261" alt="image" src="https://github.com/user-attachments/assets/3a70b847-c493-4ac8-a574-66b82ddd2b4c" />

위 사진에 나온 객체는 모두 **bs4.element** 객체에 포함돼 있다. BeautifulSoup의 find(), select() 등의 메서드를 이용했을 때 반환되는 객체는 모두  
bs4.element 내에 속해있다.(주로 bs4.element.tag)  

* **tag**: HTML 태그 그 자체('div', 'a' 등)
* **NavigableString**: 태그 안에 들어있는 순수한 '문자열'
* **comment**: HTML 주석('')
* **BeautifulSoup**: 문서 전체를 담고 있는 최상위 객체
<br/>

bs4 객체들은 Tree 구조로 연결되어 있기 때문에, 다음과 같은 관계를 가진다.  
* **부모(parent)**: 나를 감싸고 있는 바로 위 태그 (예: td의 부모는 tr)
* **자식(children)**: 내 안에 들어있는 태그나 문자열
* **형제(sibling)**: 나와 같은 층위에 있는 옆 태그들

따라서 find()나 select() 특정 객체 하나를 잡은 뒤,  
.parent, .child를 통해 위, 아래로 이동하거나 .find_next_sibling()을 써서 옆으로 이동할 수 있다.  
<br />  
**사용 예시**  
```python
html = '<td class="subject"> <a href="/post/1">교외장학</a> </td>'
soup = BeautifulSoup(html, 'html.parser')

# 1. Tag 객체 얻기
td_tag = soup.find('td') 
print(type(td_tag)) # <class 'bs4.element.Tag'>
tr_tag = td_tag.parent # tr 반환

# 2. NavigableString 객체 얻기
text_node = td_tag.a.string
print(type(text_node)) # <class 'bs4.element.NavigableString'>

# 3. 속성(Attribute) 접근 (Tag 객체의 특징)
print(td_tag['class']) # ['subject'] (리스트로 반환됨)
```
### tag
위 4가지 객체 중 가장 중요한 객체로는 **tag**를 뽑을 수 있다.  
이 객체는 BeatifulSoup를 사용할 때 가장 많이 다루는 객체이며, 스스로 데이터를 찾는 능력이 있다.  

* **.name**: 태그의 이름 (예: 'td', 'a') 등을 바꿀 수 있다.
* **.attrs**: 모든 속성을 딕셔너리 형태로 한 번에 보여준다.
* **.contents**: 자식 요소들을 리스트에 담아 보낸다.
* **.string**: 태그 안에 문자열이 단 하나 있을 경우, 이를 반환한다.
* **.text**: 내부의 모든 텍스트를 합쳐서 가져온다.(string보다 자주 사용됨.)

또한, HTML의 속성과 계층 구조를 모두 제어할 수 있는 기능이 있다.  
* **Dictionary처럼 동작**: tag['class']나 tag['href']로 속성에 바로 접근할 수 있다.
* **탐색 능력**: 자기 자신을 기준으로 .find()를 다시 호출하거나, .parent(부모), .next_sibling(옆칸)으로 이동할 수 있다.
* **변형 가능**: tag.spring = "새 제목"처럼 값을 새로 정할 수 있다.

<br />

### NavigableString
태그 내부의 텍스트를 담는 객체이다. 파이썬의 일반적인 문자열(str)과 거의 같지만,  
자신이 어느 태그에 속해있는지(parent)를 기억한다는 점에서 차이가 있다.   
.parent를 호출하면 자신이 속해있는 tag로 돌아갈 수 있다. 단, 태그 없이 문자열만 단독으로 존재할 때는 이 객체 타입이 된다.
<br />

### ResultSet  
find_all()을 사용했을 때 돌아오는 객체이다.
파이썬의 list를 상속받아 만든 **tag 전용 리스트**이다.  
리스트와 똑같이 인덱싱([])이나 for문 순회가 가능하지만, .text나 .find() 같은 메서드는 직접 사용할 수 없다.  
이를 사용하려면 요소를 하나씩 꺼내서 써야 한다.  
