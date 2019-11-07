import pymysql
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


con = pymysql.connect(host="localhost", user="root", password="ckddud950!", db="youtube_popular2", charset="utf8")
cur = con.cursor()

category = ['뉴스/정치', '엔터테인먼트', '게임', '스포츠', '인물/블로그', '노하우/스타일', '영화/애니메이션', '코미디', '음악', '과학기술', '교육', '여행/이벤트']
col = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'pink', 'black', 'darkblue', 'aqua', 'olive', 'greenyellow']

for ii in range(0, len(category) - 1):
    sql = 'select popular.timeId, popular.videoId from popular inner join (select distinct videoId, category from video) as v on popular.videoId = v.videoId where category="' + category[ii] + '"'
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

    jaccards = sorted(jaccards)
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

    plt.plot(x, y, color=col[ii], label=category[ii])
    plt.legend()
    plt.savefig('6usresult.png')

con.close()