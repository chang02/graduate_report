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
plothandler.drawLogCDF(
    [views, views2],
    ['blue', 'red'],
    ['KR', 'US'],
    [100000, 200000, 500000, 1000000, 2000000, 4000000, 8000000, 16000000],
    ['10만', '20만', '50만', '100만', '200만', '400만', '800만', '1600만'],
    '처음 인기영상에 rank되었을 때 조회수 CDF',
    '조회수',
    '누적',
    '5-4result.png'
)