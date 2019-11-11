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

likesHatesPerViewsList = []

for video in videoList:
    print('kr', video)
    sql = 'select views, likes, hates from video where views is not null and likes is not null and hates is not null and videoId = "' + video + '" order by timeId desc limit 1'
    cur.execute(sql)
    result = cur.fetchone()
    if result == None:
        continue
    else:
        likesHatesPerViewsList.append(round((result[1] + result[2]) / result[0], 4))

likesHatesPerViewsList = sorted(likesHatesPerViewsList)

x = [0]
y = [0]
temp = likesHatesPerViewsList[0]
count = 0
for data in likesHatesPerViewsList:
    if data == temp:
        count += 1
    else:
        x.append(temp)
        y.append(count / len(likesHatesPerViewsList))
        temp = data
        count += 1
x.append(temp)
y.append(count / len(likesHatesPerViewsList))
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

likesHatesPerViewsList = []

for video in videoList:
    print('us', video)
    sql = 'select views, likes, hates from video where views is not null and likes is not null and hates is not null and videoId = "' + video + '" order by timeId desc limit 1'
    cur.execute(sql)
    result = cur.fetchone()
    if result == None:
        continue
    else:
        likesHatesPerViewsList.append(round((result[1] + result[2]) / result[0], 4))

likesHatesPerViewsList = sorted(likesHatesPerViewsList)

x2 = [0]
y2 = [0]
temp = likesHatesPerViewsList[0]
count = 0
for data in likesHatesPerViewsList:
    if data == temp:
        count += 1
    else:
        x2.append(temp)
        y2.append(count / len(likesHatesPerViewsList))
        temp = data
        count += 1
x2.append(temp)
y2.append(count / len(likesHatesPerViewsList))

plt.title('조회수 대비 (좋아요 + 싫어요)의 비율 CDF (영상별로 가장 마지막 timeId)')
plt.plot(x, y, color="blue", label="KR")
plt.plot(x2, y2, color="red", label="US")
plt.legend()
plt.savefig('5-1result.png')

con.close()