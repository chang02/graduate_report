import pymysql
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

con = pymysql.connect(host="localhost", user="root", password="ckddud950!", db="youtube_popular2", charset="utf8")
cur = con.cursor()

sql = 'select videoId, timeId from popular where rank = 1'
cur.execute(sql)
result = cur.fetchall()
result = list(result)

views = []
for element in result:
    sql = 'select views from video where videoId = "' + element[0] + '" and timeId = ' + str(element[1])
    cur.execute(sql)
    result = cur.fetchone()
    if result == None or result[0] == None:
        pass
    else:
        views.append(result[0])

plt.title('특정 인기 순위(1위)에서의 조회수에 대한 boxplot(US)')
plt.xticks([1],['views'])
plt.boxplot(views, sym="bo")
plt.savefig('5-3usresult.png')

con.close()