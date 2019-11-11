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
views = []
for video in videoList:
    print('kr', video)
    sql = 'select views from video where videoId = "' + video + '" order by timeId limit 1'
    result = dbhandler.fetchone(sql)
    if result[0] != None:
        views.append(result[0])
views = sorted(views)


config = {
    "host": "localhost",
    "user": "root",
    "password": "ckddud950!",
    "db": "youtube_popular2",
}
dbhandler = DBHandler(config)
videoList = dbhandler.getMeaningVideos()
views2 = []
for video in videoList:
    print('us', video)
    sql = 'select views from video where videoId = "' + video + '" order by timeId limit 1'
    result = dbhandler.fetchone(sql)
    if result[0] != None:
        views2.append(result[0])

views2 = sorted(views2)

plothandler = plotHandler()
plothandler.drawCDF([views, views2], ['blue', 'red'], ['KR', 'US'], '처음 인기영상에 rank되었을 때 조회수 CDF', '5-4result.png')