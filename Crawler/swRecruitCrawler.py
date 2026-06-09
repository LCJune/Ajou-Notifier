import requests
from bs4 import BeautifulSoup

from baseCrawler import baseCrawler

class swRecruitCrawler(baseCrawler):
    
    def __init__(self):
        super().__init__()
        self.url = "https://software.ajou.ac.kr/bbs/board.php?tbl=bbs02"
        
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
            
            #공지 제목 추출
            title = a_tag.get("title", "제목 없음")
            
            #공지 링크 추출
            link = "https://www.ajou.ac.kr/kr/ajou/notice_scholarship.do" + a_tag.get('href', '')
            
            notices.append({
                'id': post_id,
                'title': title,
                'link': link
            })
        return notices
    
    def get_notices(self):
        data = self._crawl()
        if data is not None:
            return self._parse(data)
        else:
            return []
        
