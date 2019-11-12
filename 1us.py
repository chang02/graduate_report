import pymysql
from handler import DBHandler, plotHandler

config = {
    "host": "localhost",
    "user": "root",
    "password": "ckddud950!",
    "db": "youtube_popular2",
}
dbhandler = DBHandler(config)
sql = 'SELECT distinct videoId, category from video where category is not null'
rawResult = dbhandler.fetchall(sql)

numOfCategory = {}
for el in rawResult:
    if el[1] in numOfCategory:
        numOfCategory[el[1]] += 1
    else:
        numOfCategory[el[1]] = 1
numCategoryList = []

allCount = 0
for key, value in numOfCategory.items():
    numCategoryList.append([key, value])
    allCount += value

numCategoryList = sorted(numCategoryList, key=lambda x: x[1], reverse=True)
etc = numCategoryList[5:]
numCategoryList = numCategoryList[:5]
etcCount = 0
for el in etc:
    etcCount += el[1]
numCategoryList.append(['기타', etcCount])

plothandler = plotHandler()
plothandler.drawPie(
    [numCategoryList[0][0], numCategoryList[1][0], numCategoryList[2][0], numCategoryList[3][0], numCategoryList[4][0], numCategoryList[5][0]],
    [numCategoryList[0][1], numCategoryList[1][1], numCategoryList[2][1], numCategoryList[3][1], numCategoryList[4][1], numCategoryList[5][1]],
    ['blue', 'red', 'orange', 'yellow', 'purple', 'green'],
    '주요 카테고리 별 비율',
    '1usresult.png'
)
