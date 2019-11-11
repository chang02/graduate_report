import pymysql
from handler import DBHandler, plotHandler

# kr timeId 277 전까지는 15분 277은 22.5분 그 이후는 30분으로 친다.
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
    sql = 'select timeId from popular where videoId = "' + video + '"'
    result = dbhandler.fetchall(sql)
    time = 0
    for ele in result:
        if ele[0] < 277:
            time += 15
        elif ele[0] == 277:
            time += 22.5
        elif ele[0] > 277:
            time += 30
    timeOnPopular[video] = time
    timeOnPopularList.append(time)
timeOnPopularList = sorted(timeOnPopularList)
# -----------------------------------------------------------------------------------------------

# us timeId 93 전까지는 15분 93은 22.5분 그 이후는 30분으로 친다.
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
    sql = 'select timeId from popular where videoId = "' + video + '"'
    result = dbhandler.fetchall(sql)
    time = 0
    for ele in result:
        if ele[0] < 93:
            time += 15
        elif ele[0] == 93:
            time += 22.5
        elif ele[0] > 93:
            time += 30
    timeOnPopular[video] = time
    timeOnPopularList2.append(time)
timeOnPopularList2 = sorted(timeOnPopularList2)

plothandler = plotHandler()
plothandler.drawCDF([timeOnPopularList, timeOnPopularList2], ['blue', 'red'], ['KR', 'US'], '인기영상 리스트에 올라와있는 시간 CDF', '3result.png')