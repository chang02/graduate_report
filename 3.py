import pymysql
import matplotlib.pyplot as plt

# kr timeId 277 전까지는 15분 277은 22.5분 그 이후는 30분으로 친다.
con = pymysql.connect(host="localhost", user="root", password="ckddud950!", db="youtube_popular", charset="utf8")
cur = con.cursor()

sql = 'select distinct videoId from popular where videoId not in (select videoId from popular where timeId = 1 or timeId = 858)'
cur.execute(sql)
result = cur.fetchall()
result = list(result)
videoList = []
for element in result:
    videoList.append(element[0])

timeOnPopular = {}
timeOnPopularList = []
for video in videoList:
    sql = 'select timeId from popular where videoId = "' + video + '"'
    cur.execute(sql)
    result = cur.fetchall()
    result = list(result)
    time = 0
    for ele in result:
        if ele[0] < 277:
            time += 15
        elif ele[0] == 277:
            time += 22.5
        elif ele[0] > 277:
            time += 30
    timeOnPopular[video] = time
    timeOnPopularList.append(time)
timeOnPopularList = sorted(timeOnPopularList)

x = [0]
y = [0]
temp = timeOnPopularList[0]
count = 0
for data in timeOnPopularList:
    if data == temp:
        count += 1
    else:
        x.append(temp)
        y.append(count / len(timeOnPopularList))
        temp = data
        count += 1
x.append(temp)
y.append(count / len(timeOnPopularList))

con.close()

# -----------------------------------------------------------------------------------------------

# us timeId 93 전까지는 15분 93은 22.5분 그 이후는 30분으로 친다.
con = pymysql.connect(host="localhost", user="root", password="ckddud950!", db="youtube_popular2", charset="utf8")
cur = con.cursor()

sql = 'select distinct videoId from popular where videoId not in (select videoId from popular where timeId = 1 or timeId = 674)'
cur.execute(sql)
result = cur.fetchall()
result = list(result)
videoList = []
for element in result:
    videoList.append(element[0])

timeOnPopular = {}
timeOnPopularList = []
for video in videoList:
    sql = 'select timeId from popular where videoId = "' + video + '"'
    cur.execute(sql)
    result = cur.fetchall()
    result = list(result)
    time = 0
    for ele in result:
        if ele[0] < 93:
            time += 15
        elif ele[0] == 93:
            time += 22.5
        elif ele[0] > 93:
            time += 30
    timeOnPopular[video] = time
    timeOnPopularList.append(time)
timeOnPopularList = sorted(timeOnPopularList)

x2 = [0]
y2 = [0]
temp = timeOnPopularList[0]
count = 0
for data in timeOnPopularList:
    if data == temp:
        count += 1
    else:
        x2.append(temp)
        y2.append(count / len(timeOnPopularList))
        temp = data
        count += 1
x.append(temp)
y.append(count / len(timeOnPopularList))
plt.plot(x, y, color="blue")
plt.plot(x2, y2, color="red")
plt.savefig('3result.png')

con.close()