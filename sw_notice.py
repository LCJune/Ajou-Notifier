import request
from bs4 import BeautifulSoap

def get_software_notices():
    url = "http://software.ajou.ac.kr/bbs/board.php?tbl=bbs02"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0'}
    
    try:
        res = requests.get(url, headers=headers, timeout=10)
        
        # [수정 포인트] 서버가 주는 인코딩을 그대로 따르거나, 
        res.encoding = res.apparent_encoding # 혹은 'euc-kr'
        
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # 직접 찾으신 클래스 적용
        td_list = soup.select('td.responsive03')
        
        notices = []
        for td in td_list:
            a_tag = td.select_one('a')
            if a_tag:
                title = a_tag.get_text(strip=True)
                # 제목이 깨지지 않고 제대로 추출되었는지 확인
                notices.append({'title': title, 'link': a_tag.get('href')})
              # 아주대 구형 게시판 특성인 'euc-kr'로 설정합니다.
 
        return notices[:5]
    except Exception as e:
        print(f"에러 발생: {e}")
        return []
