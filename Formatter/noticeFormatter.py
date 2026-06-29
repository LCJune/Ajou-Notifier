from Formatter.baseFormatter import baseFormatter
from models.Notice import Notice
import datetime

class noticeFormatter(baseFormatter):
    
    @staticmethod
    def format(data):
        if not data:
            return ""
        
        if not isinstance(data[0], Notice):
            raise ValueError("지원되지 않는 데이터 타입입니다.")

        if data[0].source == "SW 채용 공지":
            formatted = f"📣 {datetime.date.today()} SW 학과 신규 채용 공지 {len(data)}건\n\n"
            for notice in data:
                formatted += f"🔹 {notice.title}\n{notice.link}\n\n"
            return formatted

        if data[0].source == "장학 공지":
            formatted = f"🎓️ {datetime.date.today()} 신규 장학 공지 {len(data)}건\n\n"
            for notice in data:
                formatted += f"🔹 {notice.title}\n{notice.link}\n\n"
            return formatted

        raise ValueError("지원되지 않는 소스입니다.")