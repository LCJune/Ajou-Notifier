import requests
from bs4 import BeautifulSoup
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import json

from Crawler.baseCrawler import baseCrawler

class scheduleCrawler(baseCrawler): # 부모 클래스를 괄호에 넣으면 자식 클래스가 된다.
    
    def __init__(self):
        super().__init__()
        self.url = "https://www.ajou.ac.kr/kr/ajou/notice-calendar.do?mode=calendar&boardNo=1021"
        
    
    def crawl(self):
        try:
            response = self.session.get(self.url, headers = self.session.headers, timeout=20)
            data = response.json().get('data', []) # JSON 응답에서 'data' 키의 값 가져오기
            
        except requests.exceptions.RequestException as e:
            print(f"에러 발생!: {e}")
            return None
        
    def parse(self, data):
        notices = []
        for item in data:
            notices.append({
                'id': item['articleNo'],
                'title': item['articleTitle'],
                'startDate': item['start'],
                'endDate': item['end'],
            })
        return notices
    
    def get_notices(self):
        data = self.crawl()
        if data is not None:
            return self.parse(data)
        else:
            return []
    