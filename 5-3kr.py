import pymysql
import matplotlib.pyplot as plt

con = pymysql.connect(host="localhost", user="root", password="ckddud950!", db="youtube_popular", charset="utf8")
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

plt.title('Box plot of views of rank 1')
plt.xticks([1],['views'])
plt.boxplot(views, sym="bo")
plt.savefig('5-3krresult.png')

con.close()