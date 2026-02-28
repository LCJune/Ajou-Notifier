import os
WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL')
import requests
import time
from datetime import datetime, timedelta
import json
from bs4 import BeautifulSoup



# 알림을 이미 보낸 일정의 ID를 저장 (중복 방지)
notified_ids = set()

def check_and_notify():
    # 1. 최신 데이터 가져오기
    url = "https://www.ajou.ac.kr/kr/ajou/notice-calendar.do?mode=calendar&boardNo=1021"
    response = requests.get(url)
    data = response.json().get('data', [])

    now = datetime.now()

    for item in data:
        # 2. 날짜 파싱 (예: '2026-03-02')
        event_date = datetime.strptime(item['start'], '%Y-%m-%d')
        event_title = item['articleTitle']
        event_id = item['articleNo'] # 고유 ID

        # 3. 시간 차이 계산 (D-Day)
        diff = event_date - now

        # 예: 일주일(7일) 전이고, 아직 알림을 보내지 않았다면
        if 6 <= diff.days < 7 and event_id not in notified_ids:
            send_slack(f"🔔 [D-7 알림] {event_title} 일정이 일주일 남았습니다!", mode = 'calendar')
            notified_ids.add(event_id)

        # 예: 전날(1일) 전일 때
        elif 0 <= diff.days < 1:
            send_slack(f"🚨 [D-1 알림] 내일은 {event_title} 입니다!", mode = 'calendar')
            notified_ids.add(event_id)

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
      response = requests.post(
          WEBHOOK_URL,
          data=json.dumps(payload),
          headers={'Content-Type': 'application/json'}
      )
      if response.status_code == 200:
          print("알림 전송 성공!")
      else:
          print(f"전송 실패: {response.status_code}")
  except Exception as e:
      print(f"An error occured: {e}")


def get_software_notices():
    url = "http://software.ajou.ac.kr/bbs/board.php?tbl=bbs02"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0'}

    try:
        res = requests.get(url, headers=headers, timeout=10)

        res.encoding = res.apparent_encoding # 아주대 소웨 게시판은 'euc-kr'

        soup = BeautifulSoup(res.text, 'html.parser')

        # 직접 찾으신 클래스 적용
        td_list = soup.select('td.responsive03') # 공지를 담고있는 td의 class

        notices = []
        for td in td_list:
            a_tag = td.select_one('a')
            if a_tag:
                title = a_tag.get_text(strip=True)
                href = a_tag.get('href', '')
                if title and href:
                    # 링크 정제
                    link = href.replace('..', 'http://software.ajou.ac.kr')
                    if 'http' not in link:
                        link = 'http://software.ajou.ac.kr' + link
                    notices.append(f"• {title}\n{link}\n\n")

        now_str = datetime.now().strftime('%Y-%m-%d %H:%M')
        message_blocks = [f"[{now_str}] 아주대 소프트웨어학과 새 소식입니다! \n\n"]

        final_message = "".join(message_blocks + notices[:3])
        
        # 2. 슬랙 전송
        send_slack(final_message, mode = 'sw')

    except Exception as e:
        print(f"에러 발생: {e}")
        return []

check_and_notify()
get_software_notices()
