import pymysql
import json
import matplotlib.pyplot as plt

def getJaccard(list1, list2):
    count = 0
    for x in list1:
        if x in list2:
            count += 1
    return round(count / (len(list1) + len(list2) - count), 4)


con = pymysql.connect(host="localhost", user="root", password="ckddud950!", db="youtube_popular", charset="utf8")
cur = con.cursor()

sql = 'select timeId, videoId from popular'
cur.execute(sql)
result = cur.fetchall()
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
for i in range(0, len(populars) - 2):
    jaccards.append(getJaccard(populars[i], populars[i+1]))

x = [0]
y = [0]
jaccards = sorted(jaccards)
temp = jaccards[0]
count = 0
for data in jaccards:
    if data == temp:
        count += 1
    else:
        x.append(temp)
        y.append(count / len(jaccards))
        temp = data
        count += 1
x.append(temp)
y.append(count / len(jaccards))

plt.plot(x, y)
plt.savefig('2krresult.png')
con.close()