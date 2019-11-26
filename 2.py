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
    "db": "youtube_popular",
}

dbhandler = DBHandler(config)
timeIds = dbhandler.getTimeIds()

sql = 'select videoId, timeId from popular where timeId in ' + str(timeIds).replace('[','(').replace(']',')')
rawResult = dbhandler.fetchall(sql)
nowTimeId = rawResult[0][1]
sets = []
temp = []
for el in rawResult:
    if el[1] == nowTimeId:
        temp.append(el[0])
    else:
        sets.append(temp)
        temp = [el[0]]
        nowTimeId = el[1]
sets.append(temp)
jaccards = []
for i in range(0, len(sets) - 1):
    jaccards.append(getJaccard(sets[i], sets[i+1]))
jaccards = sorted(jaccards)


config = {
    "host": "localhost",
    "user": "root",
    "password": "ckddud950!",
    "db": "youtube_popular2",
}

dbhandler = DBHandler(config)
timeIds = dbhandler.getTimeIds()

sql = 'select videoId, timeId from popular where timeId in ' + str(timeIds).replace('[','(').replace(']',')')
rawResult = dbhandler.fetchall(sql)
nowTimeId = rawResult[0][1]
sets = []
temp = []
for el in rawResult:
    if el[1] == nowTimeId:
        temp.append(el[0])
    else:
        sets.append(temp)
        temp = [el[0]]
        nowTimeId = el[1]
sets.append(temp)
jaccards2 = []
for i in range(0, len(sets) - 1):
    jaccards2.append(getJaccard(sets[i], sets[i+1]))
jaccards2 = sorted(jaccards2)

plothandler = plotHandler()
plothandler.drawCDF([jaccards, jaccards2], ['blue', 'red'], ['KR', 'US'], '인기 영상이 얼마나 잘 변화하는지(3시간 간격) CDF', 'Jaccard similarity', '누적', '2result.png')