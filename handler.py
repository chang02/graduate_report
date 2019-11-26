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
    
    def getMeaningVideos(self, category=None):
        if category == None:
            sql = 'select min(id) from captureTime'
            self.cur.execute(sql)
            minTimeId = self.cur.fetchone()[0]

            sql = 'select max(id) from captureTime'
            self.cur.execute(sql)
            maxTimeId = self.cur.fetchone()[0]

            sql = 'select distinct videoId from popular where videoId not in (select videoId from popular where timeId = ' + str(minTimeId) + ' or timeId = ' + str(maxTimeId) + ')'
            self.cur.execute(sql)
            rawVideoList = self.cur.fetchall()
            videoList = []
            for el in rawVideoList:
                videoList.append(el[0])
            return videoList
        else:
            sql = 'select min(id) from captureTime'
            self.cur.execute(sql)
            minTimeId = self.cur.fetchone()[0]
            
            sql = 'select max(id) from captureTime'
            self.cur.execute(sql)
            maxTimeId = self.cur.fetchone()[0]

            sql = 'select distinct videoId from video where category = "' + category +'" and videoId not in (select videoId from popular where timeId = ' + str(minTimeId) + ' or timeId = ' + str(maxTimeId) + ') and videoId in (select videoId from popular)'
            self.cur.execute(sql)
            rawVideoList = self.cur.fetchall()
            videoList = []
            for el in rawVideoList:
                videoList.append(el[0])
            return videoList
        
    def getSampleVideos(self, category):
        videos = self.getMeaningVideos(category)
        videoExist = []
        for video in videos:
            sql = 'select timeId from popular where videoId = "' + video + '"'
            rawList = self.fetchall(sql)
            time = 0
            for el in rawList:
                time += 30
            videoExist.append((time, video))
        videoExist = sorted(videoExist, key=lambda x: x[0], reverse=True)
        result = videoExist[:3]
        return [result[0][1], result[1][1], result[2][1]]
    
    def getShortTermTimeIds(self):
        sql = 'select id from captureTime where minute(time) = 30 or minute(time) = 0'
        self.cur.execute(sql)
        rawTimeList = self.cur.fetchall()
        timeList = []
        for el in rawTimeList:
            timeList.append(el[0])
        return timeList

    def getTimeIds(self):
        sql = 'select id from captureTime where minute(time) = 0 and mod(hour(time), 3) = 0'
        self.cur.execute(sql)
        rawTimeList = self.cur.fetchall()
        timeList = []
        for el in rawTimeList:
            timeList.append(el[0])
        return timeList
    
    def getRanks(self, videoId):
        sql = 'select rank from popular where videoId = "' + videoId + '"'
        self.cur.execute(sql)
        rawRanks = self.cur.fetchall()
        ranks = []
        for el in rawRanks:
            ranks.append(el[0])
        return ranks
    
    def fetchone(self, sql):
        self.cur.execute(sql)
        rawResult = self.cur.fetchone()
        return rawResult
    
    def fetchall(self, sql):
        self.cur.execute(sql)
        rawResult = self.cur.fetchall()
        return rawResult

class plotHandler:
    def drawCDF(self, lis, colors, labels, title, xlabel, ylabel, name):
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
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.savefig(name)
        plt.clf()

    def drawLogCDF(self, lis, colors, labels, xticks, xtickLabels, title, xlabel, ylabel, name):
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
        plt.xscale('log')
        plt.xticks(xticks, xtickLabels)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.savefig(name)
        plt.clf()
    
    def drawBox(self, li, x, title, name):
        plt.title(title)
        plt.xticks([1],[x])
        plt.boxplot(li, sym="bo")
        plt.savefig(name)
        plt.clf()
    
    def drawPie(self, labels, sizes, colors, title, name):
        plt.title(title)
        plt.pie(sizes, labels=labels, colors=colors, counterclock=False, startangle=90, autopct='%1.1f%%', pctdistance=0.7)
        plt.savefig(name)
        plt.clf()
    
    def drawRank(self, lis, colors, labels, title, name):
        for i in range(0, len(lis)):
            x = []
            y = []
            cnt = 0
            for value in lis[i]:
                x.append(cnt * 30)
                y.append(value)
                cnt += 1
            plt.plot(x, y, color=colors[i], label=labels[i])
        plt.legend()
        plt.gca().invert_yaxis()

        templist = []
        for li in lis:
            templist.append(len(li))
        m = max(templist)
        temp = 1440
        xticks = []
        xtickLabels = []
        i = 1
        while True:
            if temp > m * 30:
                xticks.append(temp)
                xtickLabels.append(str(i)+'일')
                break
            else:
                xticks.append(temp)
                xtickLabels.append(str(i)+'일')
                temp = temp + 1440
                i += 1

        plt.xticks(xticks, xtickLabels)
        plt.title(title)
        plt.xlabel('시간')
        plt.ylabel('순위')
        plt.savefig(name)
        plt.clf()
    
    def drawScatter(self, xs, ys, xlabel, ylabel, labels, colors, title, name):
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        for i in range(0, len(xs)):
            plt.scatter(xs[i], ys[i], color=colors[i], s=5, label=labels[i])
        plt.legend()
        plt.savefig(name)
        plt.clf()