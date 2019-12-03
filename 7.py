from handler import DBHandler, plotHandler
config = {
    "host": "localhost",
    "user": "root",
    "password": "ckddud950!",
    "db": "youtube_popular",
}
dbhandler = DBHandler(config)

categories = ['뉴스/정치', '엔터테인먼트', '코미디', '인물/블로그', '스포츠']
plothandler = plotHandler()
cnt = 0
for category in categories:
    print('kr', category)
    videos = dbhandler.getSampleVideos(category)
    rankList = []
    for video in videos:
        ranks = dbhandler.getRanks(video)
        rankList.append(ranks)
    plothandler.drawRank(rankList, ['blue', 'red', 'yellow', 'orange', 'violet'], videos, category + '의 샘플 랭크 변화(KR)', '7kr' + str(cnt) + 'result.png')
    cnt += 1


config = {
    "host": "localhost",
    "user": "root",
    "password": "ckddud950!",
    "db": "youtube_popular2",
}
dbhandler = DBHandler(config)

categories = ['엔터테인먼트', '스포츠', '음악', '코미디', '인물/블로그']
plothandler = plotHandler()
cnt = 0
for category in categories:
    print('us', category)
    videos = dbhandler.getSampleVideos(category)
    rankList = []
    for video in videos:
        ranks = dbhandler.getRanks(video)
        rankList.append(ranks)
    plothandler.drawRank(rankList, ['blue', 'red', 'yellow', 'orange', 'violet'], videos, category + '의 샘플 랭크 변화(US)', '7us' + str(cnt) + 'result.png')
    cnt += 1