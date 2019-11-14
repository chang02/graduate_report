import pymysql
from handler import DBHandler, plotHandler

config = {
    "host": "localhost",
    "user": "root",
    "password": "ckddud950!",
    "db": "youtube_popular",
}
dbhandler = DBHandler(config)
categorieskr = ['뉴스/정치', '엔터테인먼트', '코미디', '인물/블로그', '스포츠']
color = ['red', 'orange', 'yellow', 'green', 'blue']

timeOnPopularListList = []
for category in categorieskr:
    videoList = dbhandler.getMeaningVideos(category)
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
    timeOnPopularListList.append(timeOnPopularList)

plothandler = plotHandler()
plothandler.drawCDF(timeOnPopularListList, color, categorieskr, '카테고리 별 인기영상에 올라와 있는 시간 CDF(KR)', '8krresult.png')


config = {
    "host": "localhost",
    "user": "root",
    "password": "ckddud950!",
    "db": "youtube_popular2",
}
dbhandler = DBHandler(config)
categoriesus = ['엔터테인먼트', '스포츠', '코미디', '음악', '인물/블로그']
color = ['red', 'orange', 'yellow', 'green', 'blue']

timeOnPopularListList = []
for category in categoriesus:
    videoList = dbhandler.getMeaningVideos(category)
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
    timeOnPopularListList.append(timeOnPopularList)

plothandler = plotHandler()
plothandler.drawCDF(timeOnPopularListList, color, categoriesus, '카테고리 별 인기영상에 올라와 있는 시간 CDF(US)', '8usresult.png')