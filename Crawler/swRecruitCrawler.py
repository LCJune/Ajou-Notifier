import requests
from bs4 import BeautifulSoup
import re # 정규식 모듈 추가

from Crawler.baseCrawler import baseCrawler
from models.Notice import Notice

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
        tr_list = soup.find_all("tr", height = '45', bgcolor = None) # 공지사항이 담긴 tr 태그들 선택
        notices = []
        for tr in tr_list:
            # 공지 id 추출
            post_id = tr.find(class_="responsive01").get_text(strip=True)
            
            a_tag = tr.find("td",class_="responsive03").find('a')
            
            #공지 제목 추출
            title = a_tag.get_text(strip=True)
            
            #공지 링크 추출
            link = "http://software.ajou.ac.kr/bbs/board.php?tbl=bbs02" + a_tag.get('href', '')
            
            # 공지 게시일 추출
            date_posted = tr.find("p", class_ = 'tablet_regist_date').get_text(strip=True)
                
            notices.append(
                Notice(
                    id=post_id,
                    source="SW 채용 공지",
                    title=title,
                    date_posted=date_posted,
                    link=link
                )
            )
        return notices
    
    def get_notices(self):
        data = self._crawl()
        if data is not None:
            return self._parse(data)
        else:
            return []
        
sc = swRecruitCrawler()
sc.get_notices()