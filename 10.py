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


likesPerHatesList = []
for category in categorieskr:
    videoList = dbhandler.getMeaningVideos(category)
    likesPerHates = []
    for video in videoList:
        print('kr', category, video)
        sql = 'select likes, hates from video where views is not null and likes is not null and hates is not null and videoId = "' + video + '" order by timeId desc limit 1'
        result = dbhandler.fetchone(sql)
        if result == None:
            continue
        else:
            likesPerHates.append(round(result[0] / result[1], 4))
    likesPerHates = sorted(likesPerHates)
    likesPerHatesList.append(likesPerHates)

plothandler = plotHandler()
plothandler.drawCDF(likesPerHatesList, color, categorieskr, '카테고리 별로 (좋아요 / 싫어요) CDF(KR)', '10krresult.png')


config = {
    "host": "localhost",
    "user": "root",
    "password": "ckddud950!",
    "db": "youtube_popular2",
}
dbhandler = DBHandler(config)
categoriesus = ['엔터테인먼트', '스포츠', '코미디', '음악', '인물/블로그']
color = ['red', 'orange', 'yellow', 'green', 'blue']


likesPerHatesList = []
for category in categoriesus:
    videoList = dbhandler.getMeaningVideos(category)
    likesPerHates = []
    for video in videoList:
        print('us', category, video)
        sql = 'select likes, hates from video where views is not null and likes is not null and hates is not null and videoId = "' + video + '" order by timeId desc limit 1'
        result = dbhandler.fetchone(sql)
        if result == None:
            continue
        else:
            likesPerHates.append(round(result[0] / result[1], 4))
    likesPerHates = sorted(likesPerHates)
    likesPerHatesList.append(likesPerHates)

plothandler = plotHandler()
plothandler.drawCDF(likesPerHatesList, color, categoriesus, '카테고리 별로 (좋아요 / 싫어요) CDF(US)', '10usresult.png')