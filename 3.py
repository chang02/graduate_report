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
timeOnPopular = {}
timeOnPopularList = []
for video in videoList:
    print('kr', video)
    sql = 'select timeId from popular where videoId = "' + video + '"'
    result = dbhandler.fetchall(sql)
    time = 0
    for ele in result:
        time += 30
    timeOnPopular[video] = time
    timeOnPopularList.append(time)
timeOnPopularList = sorted(timeOnPopularList)
# -----------------------------------------------------------------------------------------------

config = {
    "host": "localhost",
    "user": "root",
    "password": "ckddud950!",
    "db": "youtube_popular2",
}
dbhandler = DBHandler(config)

videoList = dbhandler.getMeaningVideos()
timeOnPopular = {}
timeOnPopularList2 = []
for video in videoList:
    print('us', video)
    sql = 'select timeId from popular where videoId = "' + video + '"'
    result = dbhandler.fetchall(sql)
    time = 0
    for ele in result:
        time += 30
    timeOnPopular[video] = time
    timeOnPopularList2.append(time)
timeOnPopularList2 = sorted(timeOnPopularList2)

plothandler = plotHandler()
plothandler.drawLogCDF(
    [timeOnPopularList, timeOnPopularList2],
    ['blue', 'red'],
    ['KR', 'US'],
    [60, 360, 720, 1440, 2880, 5760, 11520],
    ['1시간', '6시간', '12시간', '1일', '2일', '4일', '8일'],
    '인기영상 리스트에 올라와있는 시간 CDF',
    '생존 기간',
    '누적',
    '3result.png'
)