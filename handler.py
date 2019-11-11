import pymysql
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

class DBHandler:
    def __init__(self, config):
        self.con = pymysql.connect(host=config['host'], user=config['user'], password=config['password'], db=config['db'], charset="utf8")
        self.cur = self.con.cursor()

    def __del__(self):
        self.con.close()

    def getAllVideos(self):
        sql = 'select distinct videoId from popular'
        self.cur.execute(sql)
        rawVideoList = self.cur.fetchall()
        videoList = []
        for el in rawVideoList:
            videoList.append(el[0])
        return videoList
    
    def getMeaningVideos(self):
        sql = 'select max(id) from captureTime'
        self.cur.execute(sql)
        maxTimeId = self.cur.fetchone()[0]

        sql = 'select distinct videoId from popular where videoId not in (select videoId from popular where timeId = 1 or timeId = '+ str(maxTimeId) +')'
        self.cur.execute(sql)
        rawVideoList = self.cur.fetchall()
        videoList = []
        for el in rawVideoList:
            videoList.append(el[0])
        return videoList
    
    def getTimeIds(self):
        sql = 'select id from captureTime where minute(time) = 0 and mod(hour(time), 2) = 0'
        self.cur.execute(sql)
        rawTimeList = self.cur.fetchall()
        timeList = []
        for el in rawTimeList:
            timeList.append(el[0])
        return timeList
    
    def fetchone(self, sql):
        self.cur.execute(sql)
        rawResult = self.cur.fetchone()
        return rawResult
    
    def fetchall(self, sql):
        self.cur.execute(sql)
        rawResult = self.cur.fetchall()
        return rawResult

class plotHandler:
    def drawCDF(self, lis, colors, labels, title, name):
        for i in range(0, len(lis)):
            x = [0]
            y = [0]
            temp = lis[i][0]
            count = 0
            for data in lis[i]:
                if data == temp:
                    count += 1
                else:
                    x.append(temp)
                    y.append(count / len(lis[i]))
                    temp = data
                    count += 1
            x.append(temp)
            y.append(count / len(lis[i]))
            plt.plot(x, y, color=colors[i], label=labels[i])
        plt.legend()
        plt.title(title)
        plt.savefig(name)