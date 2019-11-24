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
color = ['salmon', 'darkorange', 'khaki', 'springgreen', 'blueviolet']


likesHatesPerViewsListList = []
for category in categorieskr:
    videoList = dbhandler.getMeaningVideos(category)
    likesHatesPerViewsList = []
    for video in videoList:
        print('kr', category, video)
        sql = 'select views, likes, hates from video where views is not null and likes is not null and hates is not null and videoId = "' + video + '" order by timeId desc limit 1'
        result = dbhandler.fetchone(sql)
        if result == None:
            continue
        else:
            likesHatesPerViewsList.append(round((result[1] + result[2]) / result[0], 4))
    likesHatesPerViewsList = sorted(likesHatesPerViewsList)
    likesHatesPerViewsListList.append(likesHatesPerViewsList)

plothandler = plotHandler()
plothandler.drawCDF(likesHatesPerViewsListList, color, categorieskr, '카테고리 별로 조회수 대비 (좋아요 + 싫어요)의 비율 CDF(KR)', '9krresult.png')


config = {
    "host": "localhost",
    "user": "root",
    "password": "ckddud950!",
    "db": "youtube_popular2",
}
dbhandler = DBHandler(config)
categoriesus = ['엔터테인먼트', '스포츠', '코미디', '음악', '인물/블로그']
color = ['darkorange', 'blueviolet', 'khaki', 'steelblue', 'springgreen']


likesHatesPerViewsListList = []
for category in categoriesus:
    videoList = dbhandler.getMeaningVideos(category)
    likesHatesPerViewsList = []
    for video in videoList:
        print('us', category, video)
        sql = 'select views, likes, hates from video where views is not null and likes is not null and hates is not null and videoId = "' + video + '" order by timeId desc limit 1'
        result = dbhandler.fetchone(sql)
        if result == None:
            continue
        else:
            likesHatesPerViewsList.append(round((result[1] + result[2]) / result[0], 4))
    likesHatesPerViewsList = sorted(likesHatesPerViewsList)
    likesHatesPerViewsListList.append(likesHatesPerViewsList)

plothandler = plotHandler()
plothandler.drawCDF(likesHatesPerViewsListList, color, categoriesus, '카테고리 별로 조회수 대비 (좋아요 + 싫어요)의 비율 CDF(US)', '9usresult.png')