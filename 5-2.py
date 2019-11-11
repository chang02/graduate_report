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
likesPerHates = []

for video in videoList:
    print('kr', video)
    sql = 'select likes, hates from video where views is not null and likes is not null and hates is not null and videoId = "' + video + '" order by timeId desc limit 1'
    result = dbhandler.fetchone(sql)
    if result == None:
        continue
    else:
        likesPerHates.append(round(result[0] / result[1], 4))

likesPerHates = sorted(likesPerHates)

# ----------------------------------------------------------------------------------

config = {
    "host": "localhost",
    "user": "root",
    "password": "ckddud950!",
    "db": "youtube_popular2",
}
dbhandler = DBHandler(config)

videoList = dbhandler.getMeaningVideos()
likesPerHates2 = []

for video in videoList:
    print('us', video)
    sql = 'select likes, hates from video where views is not null and likes is not null and hates is not null and videoId = "' + video + '" order by timeId desc limit 1'
    result = dbhandler.fetchone(sql)
    if result == None:
        continue
    else:
        likesPerHates2.append(round(result[0] / result[1], 4))

likesPerHates2 = sorted(likesPerHates2)

plothandler = plotHandler()
plothandler.drawCDF([likesPerHates, likesPerHates2], ['blue', 'red'], ['KR', 'US'], '(좋아요 / 싫어요) CDF (영상별로 가장 마지막 timeId)', '5-2result.png')