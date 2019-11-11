import pymysql
from handler import DBHandler, plotHandler

def getJaccard(list1, list2):
    count = 0
    for x in list1:
        if x in list2:
            count += 1
    return round(count / (len(list1) + len(list2) - count), 4)

config = {
    "host": "localhost",
    "user": "root",
    "password": "ckddud950!",
    "db": "youtube_popular2",
}
dbhandler = DBHandler(config)
timeIds = dbhandler.getTimeIds()

category = ['엔터테인먼트', '스포츠', '코미디', '음악', '인물/블로그']
col = ['red', 'orange', 'yellow', 'green', 'blue']

jaccardsList = []
for ii in range(0, len(category)):
    sql = 'select popular.timeId, popular.videoId from popular inner join (select distinct videoId, category from video) as v on popular.videoId = v.videoId where category="' + category[ii] + '" and timeId in ' + str(timeIds).replace('[','(').replace(']',')')
    result = dbhandler.fetchall(sql)
    timeId = result[0][0]
    populars = []
    temp = []
    for ele in result:
        if ele[0] == timeId:
            temp.append(ele[1])
        else:
            populars.append(temp)
            timeId = ele[0]
            temp = [ele[1]]
    populars.append(temp)

    jaccards = []
    for i in range(0, len(populars) - 1):
        jaccards.append(getJaccard(populars[i], populars[i+1]))
    jaccards = sorted(jaccards)
    jaccardsList.append(jaccards)

plothandler = plotHandler()
plothandler.drawCDF(jaccardsList, col, category, '카테고리 별로 인기 영상 얼마나 잘 변화하는지 CDF(US)', '6usresult.png')