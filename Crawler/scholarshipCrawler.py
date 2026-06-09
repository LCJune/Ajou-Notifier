import requests
from bs4 import BeautifulSoup
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

from Crawler.baseCrawler import baseCrawler

class scholarshipCrawler(baseCrawler):
    
    def __init__(self):
        super().__init__()
        self.url = "https://www.ajou.ac.kr/kr/ajou/notice_scholarship.do"
        
    def crawl(self):
        try:
            response = self.session.get(self.url, headrs = self.session.headers, timeout=20)
            response.encoding = response.apparent_encoding
            soup = BeautifulSoup(response.text, 'html.parser')
            
            
        except requests.exceptions.RequestException as e:
            print(f"에러 발생!: {e}")
            return None