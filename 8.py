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
color = ['crimson', 'darkorange', 'khaki', 'springgreen', 'blueviolet']

timeOnPopularListList = []
for category in categorieskr:
    videoList = dbhandler.getMeaningVideos(category)
    timeOnPopular = {}
    timeOnPopularList = []
    for video in videoList:
        print('kr', category, video)
        sql = 'select timeId from popular where videoId = "' + video + '"'
        result = dbhandler.fetchall(sql)
        time = 0
        for ele in result:
            time += 30
        timeOnPopular[video] = time
        timeOnPopularList.append(time)
    timeOnPopularList = sorted(timeOnPopularList)
    timeOnPopularListList.append(timeOnPopularList)

plothandler = plotHandler()
plothandler.drawLogCDF(
    timeOnPopularListList,
    color,
    categorieskr,
    [60, 360, 720, 1440, 2880, 5760, 11520],
    ['1시간', '6시간', '12시간', '1일', '2일', '4일', '8일'],
    '카테고리 별 인기영상에 올라와 있는 시간 CDF(KR)(Log)',
    '생존 기간',
    '누적',
    '8krresult.png'
)


config = {
    "host": "localhost",
    "user": "root",
    "password": "ckddud950!",
    "db": "youtube_popular2",
}
dbhandler = DBHandler(config)
categoriesus = ['엔터테인먼트', '스포츠', '코미디', '음악', '인물/블로그']
color = ['darkorange', 'blueviolet', 'khaki', 'steelblue', 'springgreen']

timeOnPopularListList = []
for category in categoriesus:
    videoList = dbhandler.getMeaningVideos(category)
    timeOnPopular = {}
    timeOnPopularList = []
    for video in videoList:
        print('us', category, video)
        sql = 'select timeId from popular where videoId = "' + video + '"'
        result = dbhandler.fetchall(sql)
        time = 0
        for ele in result:
            time += 30
        timeOnPopular[video] = time
        timeOnPopularList.append(time)
    timeOnPopularList = sorted(timeOnPopularList)
    timeOnPopularListList.append(timeOnPopularList)

plothandler = plotHandler()
plothandler.drawLogCDF(
    timeOnPopularListList,
    color,
    categoriesus,
    [60, 360, 720, 1440, 2880, 5760, 11520],
    ['1시간', '6시간', '12시간', '1일', '2일', '4일', '8일'],
    '카테고리 별 인기영상에 올라와 있는 시간 CDF(US)(Log)',
    '생존 기간',
    '누적',
    '8usresult.png'
)