```python
import requests
import time
from datetime import datetime, timedelta
import json

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
            send_slack(f"🔔 [D-7 알림] {event_title} 일정이 일주일 남았습니다!")
            notified_ids.add(event_id)

        # 예: 전날(1일) 전일 때
        elif 0 <= diff.days < 1:
            send_slack(f"🚨 [D-1 알림] 내일은 {event_title} 입니다!")
            notified_ids.add(event_id)


# 발급받은 URL을 여기에 넣으세요 (유출되지 않도록 주의!)
WEBHOOK_URL = "WebHookToken"

def send_slack(msg):
    """슬랙 채널로 메시지 전송"""
    payload = {
        "text": msg,
        "username": "아주대 봇",  # 슬랙에 표시될 이름
        "icon_emoji": ":calendar:" # 아이콘 모양
    }
    
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

# 테스트 실행
send_slack("🚀 학사일정 감시 프로그램이 정상적으로 시작되었습니다!")

# 4. 주기적 실행 (예: 1시간마다)
while True:
    print(f"[{datetime.now()}] 스캔 시작...")
    check_and_notify()
    time.sleep(3600) # 3600초(1시간) 대기

```
