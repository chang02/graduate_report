# 뉴스/정치 cD2EF2XjEUc, WhZsPuOp2-E
# 엔터테인먼트 F3bUqctB9mE, 2KtFPjSp3og
# 코미디 riQGjcw4sMk, 7iNsrsP-g7I
# 인물/블로그 XohD4xOZhr4, jEA3p1ekzSw
# 스포츠 FN49Fxt3O_4, xn5hlu_pisY
import pymysql
from handler import DBHandler, plotHandler

config = {
    "host": "localhost",
    "user": "root",
    "password": "ckddud950!",
    "db": "youtube_popular",
}
dbhandler = DBHandler(config)

categories = ['뉴스/정치', '엔터테인먼트', '코미디', '인물/블로그', '스포츠']
sample = {
    "뉴스/정치": ['cD2EF2XjEUc', 'WhZsPuOp2-E'],
    "엔터테인먼트": ['F3bUqctB9mE', '2KtFPjSp3og'],
    "코미디": ['riQGjcw4sMk', '7iNsrsP-g7I'],
    "인물/블로그": ['XohD4xOZhr4', 'jEA3p1ekzSw'],
    "스포츠": ['FN49Fxt3O_4', 'xn5hlu_pisY'],
}

plothandler = plotHandler()
cnt = 0
for category in categories:
    rankList = []
    for video in sample[category]:
        ranks = dbhandler.getRanks(video)
        rankList.append(ranks)
    plothandler.drawRank(rankList, ['blue', 'red'], sample[category], category + '의 샘플 랭크 변화', '4-2kr' + str(cnt) + 'result.png')
    cnt += 1
