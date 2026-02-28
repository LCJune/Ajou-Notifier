import os
WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL')
import requests
import time
from datetime import datetime, timedelta
import json
from bs4 import BeautifulSoup

# 환경 변수 및 설정
WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL')
CALENDAR_DB = "last_calendar_ids.txt"
SW_DB = "last_sw_id.txt"

# --- 파일에서 기존 ID 로드 함수 ---
def load_ids(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return set(f.read().splitlines())
    return set()

# --- 파일에 새로운 ID 저장 함수 ---
def save_ids(filename, ids):
    with open(filename, 'w') as f:
        f.write("\n".join(map(str, ids)))
        
def send_slack(msg, mode):
  if mode == 'calendar':
    payload = {
        "text": msg,
        "username": "아주대 봇",  # 슬랙에 표시될 이름
    }
  
  if mode == 'sw':
    payload = { 
      "text": msg, 
      "username": "아주대 봇",
    }
  
  if mode == 'scholar':
    pass

  try:
      res = requests.post(
          WEBHOOK_URL,
          data=json.dumps(payload),
          headers={'Content-Type': 'application/json'}
      )
      if res.status_code == 200:
          print("알림 전송 성공!")
      else:
          print(f"전송 실패: {res.status_code}")
  except Exception as e:
      print(f"An error occured: {e}")

def check_and_notify():
    # 1. 이전 알림 ID 로드
    notified_ids = load_ids(CALENDAR_DB)
    
    # 2. 최신 데이터 가져오기
    url = "https://www.ajou.ac.kr/kr/ajou/notice-calendar.do?mode=calendar&boardNo=1021"
    res = requests.get(url)
    data = res.json().get('data', [])

    now = datetime.now()
    unnotified = []
    for item in data:
        # 3. 날짜 파싱 (예: '2026-03-02')
        event_date = datetime.strptime(item['start'], '%Y-%m-%d')
        event_title = item['articleTitle']
        event_id = item['articleNo'] # 고유 ID

        # 4. 시간 차이 계산 (D-Day)
        diff = event_date - now

        # 5. 일주일(7일) 전이고, 아직 알림을 보내지 않았다면 알림 발송
        if 6 <= diff.days < 7 and event_id not in notified_ids:
            send_slack(f"🔔 [D-7 알림] {event_title} 일정이 일주일 남았습니다!", mode = 'calendar')
            notified_ids.add(event_id)
            unnotified.append(event_id)
        # 6. 전날(1일) 알림 발송
        elif 0 <= diff.days <= 1:
            send_slack(f"🚨 [D-1 알림] 내일은 {event_title} 입니다!", mode = 'calendar')
            
    # 7. 새로 추가된 글 id 저장            
    if len(unnotified) > 0:
        save_ids(CALENDAR_DB, unnotified)

def get_software_notices():
    # 1. 이전 최신 글 ID 로드
    last_sw_id = list(load_ids(SW_DB))[0] if load_ids(SW_DB) else ""
    
    url = "http://software.ajou.ac.kr/bbs/board.php?tbl=bbs02"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0'}

    try:
        res = requests.get(url, headers=headers, timeout=10)
        res.encoding = res.apparent_encoding # 아주대 소웨 게시판은 'euc-kr'
        soup = BeautifulSoup(res.text, 'html.parser')

        td_list = soup.select('td.responsive03') # 공지를 담고있는 td의 class

        new_posts = []
        for td in td_list:
            a_tag = td.select_one('a')
            if a_tag:
                title = a_tag.get_text(strip=True)
                href = a_tag.get('href', '')
                # 1. 글 번호 추출 (고유 ID)
                post_id = href.split('num=')[1].split('&')[0] if 'num=' in href else href
                
                if post_id == last_sw_id: # 이전에 본 글을 만나면 중단
                    break

                # 2. 링크 정제
                link = href.replace('..', 'http://software.ajou.ac.kr')
                if 'http' not in link: link = 'http://software.ajou.ac.kr' + link
                new_posts.append(f"• {title}\n{link}")

        if new_posts:
            now_str = datetime.now().strftime('%Y-%m-%d %H:%M')
            msg = f"[{now_str}] SW학과 새 소식 ({len(new_posts)}건)!\n\n" + "\n".join(new_posts)    
            
            # 3. 최신 글 알림 전송
            if send_slack(msg, mode='sw'):
                # 가장 최신글 ID 저장
                save_ids(SW_DB, [new_posts[0].split('num=')[1].split('&')[0]])

        
    except Exception as e:
        print(f"에러 발생: {e}")
        return []

check_and_notify()
get_software_notices()
