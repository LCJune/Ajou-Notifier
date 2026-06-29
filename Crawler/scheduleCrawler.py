import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

from Crawler.baseCrawler import baseCrawler
from models.Schedule import Schedule

class scheduleCrawler(baseCrawler): # 부모 클래스를 괄호에 넣으면 자식 클래스가 된다.
    
    def __init__(self):
        super().__init__()
        self.url = "https://www.ajou.ac.kr/kr/ajou/notice-calendar.do?mode=calendar&boardNo=1021"
        
    
    def _crawl(self):
        try:
            response = self.session.get(self.url, headers = self.session.headers, timeout=20)
            data = response.json().get('data', []) # JSON 응답에서 'data' 키의 값 가져오기
            return data
        
        except requests.exceptions.RequestException as e:
            print(f"에러 발생!: {e}")
            return None
        
    def _parse(self, data):    
        schedule = []
        for notice in data:
            schedule.append(Schedule(
                id = notice['articleNo'],
                title=notice['articleTitle'],
                startDate = datetime.strptime(notice['start'], "%Y-%m-%d").date(),
                endDate = datetime.strptime(notice['end'], "%Y-%m-%d").date()
            ))
        return schedule
    
    def get_notices(self):
        data = self._crawl()
        if data is not None:
            return self._parse(data)
        else:
            return []
