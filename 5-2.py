import pymysql
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

con = pymysql.connect(host="localhost", user="root", password="ckddud950!", db="youtube_popular", charset="utf8")
cur = con.cursor()

sql = 'select distinct videoId from popular where videoId not in (select videoId from popular where timeId = 1 or timeId = 858)'
cur.execute(sql)
result = cur.fetchall()
result = list(result)

videoList = []

for element in result:
    videoList.append(element[0])

likesPerHates = []

for video in videoList:
    print('kr', video)
    sql = 'select likes, hates from video where views is not null and likes is not null and hates is not null and videoId = "' + video + '" order by timeId desc limit 1'
    cur.execute(sql)
    result = cur.fetchone()
    if result == None:
        continue
    else:
        likesPerHates.append(round(result[0] / result[1], 4))

likesPerHates = sorted(likesPerHates)

x = [0]
y = [0]
temp = likesPerHates[0]
count = 0
for data in likesPerHates:
    if data == temp:
        count += 1
    else:
        x.append(temp)
        y.append(count / len(likesPerHates))
        temp = data
        count += 1
x.append(temp)
y.append(count / len(likesPerHates))
con.close()

# ----------------------------------------------------------------------------------

con = pymysql.connect(host="localhost", user="root", password="ckddud950!", db="youtube_popular2", charset="utf8")
cur = con.cursor()

sql = 'select distinct videoId from popular where videoId not in (select videoId from popular where timeId = 1 or timeId = 674)'
cur.execute(sql)
result = cur.fetchall()
result = list(result)

videoList = []

for element in result:
    videoList.append(element[0])

likesPerHates = []

for video in videoList:
    print('us', video)
    sql = 'select likes, hates from video where views is not null and likes is not null and hates is not null and videoId = "' + video + '" order by timeId desc limit 1'
    cur.execute(sql)
    result = cur.fetchone()
    if result == None:
        continue
    else:
        likesPerHates.append(round(result[0] / result[1], 4))

likesPerHates = sorted(likesPerHates)

x2 = [0]
y2 = [0]
temp = likesPerHates[0]
count = 0
for data in likesPerHates:
    if data == temp:
        count += 1
    else:
        x2.append(temp)
        y2.append(count / len(likesPerHates))
        temp = data
        count += 1
x2.append(temp)
y2.append(count / len(likesPerHates))

plt.title('(좋아요 / 싫어요) CDF (영상별로 가장 마지막 timeId)')
plt.plot(x, y, color="blue", label="KR")
plt.plot(x2, y2, color="red", label="US")
plt.legend()
plt.savefig('5-2result.png')

con.close()