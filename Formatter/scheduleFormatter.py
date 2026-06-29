from Formatter.baseFormatter import baseFormatter
from models.Schedule import Schedule
from datetime import datetime, timedelta

class scheduleFormatter(baseFormatter):
    def __init__(self):
        super().__init__()
    
    @staticmethod
    def format(data):
        if not data:
            return ""
        if not isinstance(data[0], Schedule):
            raise ValueError("지원되지 않는 데이터 타입입니다.")
        
        today = datetime.now().date()
        today_schedule = f"📅 학사 일정 공지({today.strftime('%Y-%m-%d')}) 📅\n\n"
        D_7 = f"\n🔔 D-7 알림 🔔\n\n"
        D_1 = f"\n🚨 D-1 알림 🚨\n\n"
        
        tomorrow_schedules = 0
        next_week_schedules = 0
        
        for schedule in data:
            if today >= schedule.startDate and today <= schedule.endDate:
                today_schedule += f"🔹 {schedule.title} ~ {schedule.endDate}\n "
            
            if today + timedelta(days=1) == schedule.startDate:
                tomorrow_schedules += 1
                D_1 += f"🔹 {schedule.title}\n"
                
            if today + timedelta(days=7) == schedule.startDate:
                next_week_schedules += 1
                D_7 += f"🔹 {schedule.title}\n"
                
        return today_schedule + (D_1 if tomorrow_schedules > 0 else "") + (D_7 if next_week_schedules > 0 else "")

