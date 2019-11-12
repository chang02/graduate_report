# 엔터테인먼트 UAlIq7BKNxg, P2TiRJXWvHM
# 스포츠 qjsU5876iB0, yTT58uuW8uk
# 코미디 PTdQo29sv2o, UJ_h3bnwoAM
# 음악 zlJDTxahav0, 8u-_64S7plI
# 인물/블로그 efs3QRr8LWw, wjaIRPAxGgA

import pymysql
from handler import DBHandler, plotHandler

config = {
    "host": "localhost",
    "user": "root",
    "password": "ckddud950!",
    "db": "youtube_popular2",
}
dbhandler = DBHandler(config)

categories = ['엔터테인먼트', '스포츠', '코미디', '음악', '인물/블로그']
sample = {
    "엔터테인먼트": ['UAlIq7BKNxg', 'P2TiRJXWvHM'],
    "스포츠": ['qjsU5876iB0', 'yTT58uuW8uk'],
    "코미디": ['PTdQo29sv2o', 'UJ_h3bnwoAM'],
    "음악": ['zlJDTxahav0', '8u-_64S7plI'],
    "인물/블로그": ['efs3QRr8LWw', 'wjaIRPAxGgA'],
}

plothandler = plotHandler()
cnt = 0
for category in categories:
    rankList = []
    for video in sample[category]:
        ranks = dbhandler.getRanks(video)
        rankList.append(ranks)
    plothandler.drawRank(rankList, ['blue', 'red'], sample[category], category + '의 샘플 랭크 변화', '4-2us' + str(cnt) + 'result.png')
    cnt += 1