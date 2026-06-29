from Crawler import scheduleCrawler, scholarshipCrawler, swRecruitCrawler
from Formatter import noticeFormatter, scheduleFormatter
import slackSender


slack = slackSender.slackSender()
scheCrawler = scheduleCrawler.scheduleCrawler()
scholarCrawler = scholarshipCrawler.scholarshipCrawler()
swReCrawler = swRecruitCrawler.swRecruitCrawler()

# 모듈.클래스.staticmethod
scheMessage = scheduleFormatter.scheduleFormatter.format(scheCrawler.get_notices())
scholarshipMessage = noticeFormatter.noticeFormatter.format(scholarCrawler.get_notices())
swReMessage = noticeFormatter.noticeFormatter.format(swReCrawler.get_notices())

message = scheMessage + "\n" + scholarshipMessage + "\n" + swReMessage
slack.send_message(message)
