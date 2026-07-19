# Ajou-Notifier - 아주대학교 공지 알리미
아주대학교 홈페이지 게시판에 새로 게시된 글을 읽어와 Slack 메세지로 전송해주는 파이썬 프로그램입니다.

## 주요 라이브러리
### 1.request
웹 사이트에 HTTP 요청을 보내기 위해 사용

### 2. BeautifulSoup
크롤링한 HTML 정보들을 파싱(Parsing)하기 위해 사용

### 3. SQLite
읽어 온 공지들의 정보를 저장하고 관리하기 위해 사용
 
## Class 역할
### Notice
공지의 정보를 담는 class

### Schedule
일정에 대한 정보를 담는 class

### Crawler
http 사이트로부터 html 정보를 crawling해온 후, parsing하여 반환함.

### Formatter
전달받은 객체가 Notice인지, Schedule인지에 따라 알맞은 형식의 문자열을 제작함.

### SQLiteRepository
SQLite 객체의 생성 및 DB 조작을 담당하는 class
