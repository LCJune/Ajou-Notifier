from Crawler import scheduleCrawler, scholarshipCrawler, swRecruitCrawler
from Formatter import noticeFormatter, scheduleFormatter
from Repository.SQLiteRepository import SQLiteRepository
import slackSender


slack = slackSender.slackSender()
scheCrawler = scheduleCrawler.scheduleCrawler()
scholarCrawler = scholarshipCrawler.scholarshipCrawler()
swReCrawler = swRecruitCrawler.swRecruitCrawler()

schedules = scheCrawler.get_notices()
scholar_Notices = scholarCrawler.get_notices()
swRecruit_Notices = swReCrawler.get_notices()

sql = SQLiteRepository(db_path= "database/sqliteNotice.db")

scholar_filtered = []
for notice in scholar_Notices:
    if not sql.exsist(notice.id):
        scholar_filtered.append(notice)
        sql.insert(notice.id, notice.source, notice.title, notice.date_posted, notice.link)

swRecruit_filtered = []
for notice in swRecruit_Notices:
    if not sql.exsist(notice.id):
        swRecruit_filtered.append(notice)
        sql.insert(notice.id, notice.source, notice.title, notice.date_posted, notice.link)

sql.close()


# 모듈.클래스.staticmethod
scheMessage = scheduleFormatter.scheduleFormatter.format(schedules)
scholarshipMessage = noticeFormatter.noticeFormatter.format(scholar_filtered)
swReMessage = noticeFormatter.noticeFormatter.format(swRecruit_filtered)


message = scheMessage + "\n" + scholarshipMessage + "\n" + swReMessage
slack.send_message(message)

