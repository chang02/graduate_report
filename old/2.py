import pymysql
import json
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

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
for i in range(0, len(populars) - 1):
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
con.close()

#------------------------------------------------------------------------

con = pymysql.connect(host="localhost", user="root", password="ckddud950!", db="youtube_popular2", charset="utf8")
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
for i in range(0, len(populars) - 1):
    jaccards.append(getJaccard(populars[i], populars[i+1]))

x2 = [0]
y2 = [0]
jaccards = sorted(jaccards)
temp = jaccards[0]
count = 0
for data in jaccards:
    if data == temp:
        count += 1
    else:
        x2.append(temp)
        y2.append(count / len(jaccards))
        temp = data
        count += 1
x2.append(temp)
y2.append(count / len(jaccards))

plt.title('인기 영상이 얼마나 잘 변화하는지 CDF')
plt.plot(x, y, color="blue", label="KR")
plt.plot(x2, y2, color="red", label="US")
plt.legend()
plt.savefig('2result.png')
con.close()