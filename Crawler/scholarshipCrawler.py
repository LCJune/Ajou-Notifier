import requests
from bs4 import BeautifulSoup
import re # 정규식 모듈 추가

from Crawler.baseCrawler import baseCrawler
from models.Notice import Notice

class scholarshipCrawler(baseCrawler):
    
    def __init__(self):
        super().__init__()
        self.url = "https://www.ajou.ac.kr/kr/ajou/notice_scholarship.do"
        
    def _crawl(self):
        try:
            response = self.session.get(self.url, headers = self.session.headers, timeout=20)
            response.encoding = response.apparent_encoding # 실제 페이지의 인코딩 방식 추정해서 사용
            return response
        
        except requests.exceptions.RequestException as e:
            print(f"에러 발생!: {e}")
            return None
        
        
    def _parse(self, data):
        soup = BeautifulSoup(data.text, 'html.parser')
        tr_list = soup.find_all('tr', class_='')
        
        notices = []
        for tr in tr_list:
            # 공지 id 추출
            post_id = tr.find(class_="b-num-box").get_text(strip=True)
            
            a_tag = tr.find(class_="b-title-box").find('a')
            
            # 공지 제목 추출
            title = a_tag.get("title", "제목 없음")
            
            # 공지 링크 추출
            link = "https://www.ajou.ac.kr/kr/ajou/notice_scholarship.do" + a_tag.get('href', '')
            
            # 공지 게시일 추출
            date_posted = None # 날짜 정보가 없는 경우 None으로 설정
            
            for td in tr.find_all('td', class_=None):
                text = td.get_text(strip=True)
                
                # python의 raw string을 사용하여 정규식 패턴을 작성. \d는 숫자를 의미하며, {4}는 4자리, {2}는 2자리를 의미. \d{4}\-\d{2}\-\d{2}는 "YYYY-MM-DD" 형식의 날짜를 나타냄.
                if re.fullmatch(r'\d{4}\-\d{2}\-\d{2}', text): 
                    date_posted = text
                    break
                
            
            notices.append(
                Notice(
                    id=post_id,
                    source="장학 공지",
                    title=title,
                    date_posted=date_posted,
                    link=link
                )
            )
        print(notices[0].id, notices[0].source, notices[0].title, notices[0].date_posted, notices[0].link)
        return notices
    
    def get_notices(self):
        data = self._crawl()
        if data is not None:
            return self._parse(data)
        else:
            return []

sc = scholarshipCrawler()
notices = sc.get_notices()