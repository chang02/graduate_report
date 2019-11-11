import pymysql
from handler import DBHandler, plotHandler

config = {
    "host": "localhost",
    "user": "root",
    "password": "ckddud950!",
    "db": "youtube_popular",
}
dbhandler = DBHandler(config)

videoList = dbhandler.getMeaningVideos()
likesHatesPerViewsList = []

for video in videoList:
    print('kr', video)
    sql = 'select views, likes, hates from video where views is not null and likes is not null and hates is not null and videoId = "' + video + '" order by timeId desc limit 1'
    result = dbhandler.fetchone(sql)
    if result == None:
        continue
    else:
        likesHatesPerViewsList.append(round((result[1] + result[2]) / result[0], 4))

likesHatesPerViewsList = sorted(likesHatesPerViewsList)

# ----------------------------------------------------------------------------------
config = {
    "host": "localhost",
    "user": "root",
    "password": "ckddud950!",
    "db": "youtube_popular2",
}
dbhandler = DBHandler(config)

videoList = dbhandler.getMeaningVideos()
likesHatesPerViewsList2 = []
for video in videoList:
    print('us', video)
    sql = 'select views, likes, hates from video where views is not null and likes is not null and hates is not null and videoId = "' + video + '" order by timeId desc limit 1'
    result = dbhandler.fetchone(sql)
    if result == None:
        continue
    else:
        likesHatesPerViewsList2.append(round((result[1] + result[2]) / result[0], 4))

likesHatesPerViewsList2 = sorted(likesHatesPerViewsList2)

plothandler = plotHandler()
plothandler.drawCDF([likesHatesPerViewsList, likesHatesPerViewsList2], ['blue', 'red'], ['KR', 'US'], '조회수 대비 (좋아요 + 싫어요)의 비율 CDF (영상별로 가장 마지막 timeId)', '5-1result.png')