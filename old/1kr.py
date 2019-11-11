import pymysql
import json

con = pymysql.connect(host="localhost", user="root", password="ckddud950!", db="youtube_popular", charset="utf8")
cur = con.cursor()
sql = 'SELECT distinct popular.videoId, v.category from popular inner join (select distinct videoId, category from video) as v on popular.videoId = v.videoId'
cur.execute(sql)
result = cur.fetchall()
result = list(result)
obj = {}
for ele in result:
    if ele[1] != None:
        obj[ele[0]] = ele[1]
distinctRatioObject = {}

for key, value in obj.items():
    if value in distinctRatioObject:
        distinctRatioObject[value] += 1
    else:
        distinctRatioObject[value] = 1

sql = 'select videoId from popular'
cur.execute(sql)
result = cur.fetchall()
result = list(result)
uniqueRatioObject = {}
for ele in result:
    category = obj[ele[0]]
    if category in uniqueRatioObject:
        uniqueRatioObject[category] += 1
    else:
        uniqueRatioObject[category] = 1

div = 0
for value in distinctRatioObject.values():
    div += value
for key in distinctRatioObject.keys():
    distinctRatioObject[key] = round(distinctRatioObject[key] / div, 4)
div = 0
for value in uniqueRatioObject.values():
    div += value
for key in uniqueRatioObject.keys():
    uniqueRatioObject[key] = round(uniqueRatioObject[key] / div, 4)
print('같은 비디오는 1개로 취급했을 때')
print(distinctRatioObject)
print('각각의 비디오를 다 unique하게 취급했을 때')
print(uniqueRatioObject)

con.close()