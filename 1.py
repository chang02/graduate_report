import pymysql
from handler import DBHandler

config = {
    "host": "localhost",
    "user": "root",
    "password": "ckddud950!",
    "db": "youtube_popular",
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
for el in numCategoryList:
    el[1] = round(el[1] / allCount, 4)
print('KR')
print(numCategoryList)



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
for el in numCategoryList:
    el[1] = round(el[1] / allCount, 4)
print('US')
print(numCategoryList)