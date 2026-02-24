```python
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

# 1. 세션 생성 및 공통 헤더 설정
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0',
    'Content-Type': 'application/x-www-form-urlencoded' # POST 요청 시 필수
})

def get_ajou_calendar(target_date=None):
    """
    target_date: '2026-03-01' 형식의 문자열.
                 입력하지 않으면 현재 날짜 기준.
    """
    base_url = "https://www.ajou.ac.kr/kr/ajou/notice-calendar.do"

    # 1. 날짜가 없으면 오늘 기준으로 생성
    if not target_date:
        target_date = datetime.now().strftime('%Y-%m-01')

    # 2. 파라미터 구조화 (주소를 고정하지 않음)
    params = {
        'mode': 'calendar',
        'boardNo': '1021',
        'date': target_date,
        'srCategoryId': '',
        '_': int(time.time() * 1000)  # 현재 시간을 타임스탬프로 변환
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0'
    }

    # 3. 요청 시 params를 넣어주면 자동으로 URL 완성
    response = requests.get(base_url, headers=headers, params=params)

    return response.json()

march_data = get_ajou_calendar()
for item in march_data.get('data', []):
    print(f"[{item['startDt']}] {item['articleTitle']}")
```
