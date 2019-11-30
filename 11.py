from handler import DBHandler, plotHandler

config = {
    "host": "localhost",
    "user": "root",
    "password": "ckddud950!",
    "db": "youtube_popular",
}
dbhandler = DBHandler(config)
categories = ['뉴스/정치', '엔터테인먼트', '코미디', '인물/블로그', '스포츠']
colors = ['crimson', 'darkorange', 'khaki', 'springgreen', 'blueviolet']
xs = []
ys = []

for category in categories:
    tempx = []
    tempy = []
    videoList = dbhandler.getMeaningVideos(category)
    for video in videoList:
        print('kr', category, video)
        sql = 'select rank from popular where videoId = "' + video + '"'
        rawRanks = dbhandler.fetchall(sql)
        deltaRank = 0
        deltaAbsRank = 0
        for i in range(0, len(rawRanks) - 1):
            deltaRank += rawRanks[i+1][0] - rawRanks[i][0]
            deltaAbsRank += abs(rawRanks[i+1][0] - rawRanks[i][0])
        if deltaAbsRank < 200:
            tempx.append(deltaRank)
            tempy.append(deltaAbsRank)
    xs.append(tempx)
    ys.append(tempy)

plothandler = plotHandler()
plothandler.drawScatter(xs, ys, 'rank 변화', 'abs(rank) 변화', categories, colors, '각 비디오에 대해서 abs(rank) 변화, rank(변화) scatter(KR)', '11krresult.png')


config = {
    "host": "localhost",
    "user": "root",
    "password": "ckddud950!",
    "db": "youtube_popular2",
}
dbhandler = DBHandler(config)
categories = ['엔터테인먼트', '스포츠', '음악', '코미디', '인물/블로그']
color = ['darkorange', 'blueviolet', 'olive', 'khaki', 'springgreen']
xs = []
ys = []

for category in categories:
    tempx = []
    tempy = []
    videoList = dbhandler.getMeaningVideos(category)
    for video in videoList:
        print('us', category, video)
        sql = 'select rank from popular where videoId = "' + video + '"'
        rawRanks = dbhandler.fetchall(sql)
        deltaRank = 0
        deltaAbsRank = 0
        for i in range(0, len(rawRanks) - 1):
            deltaRank += rawRanks[i+1][0] - rawRanks[i][0]
            deltaAbsRank += abs(rawRanks[i+1][0] - rawRanks[i][0])
        tempx.append(deltaRank)
        tempy.append(deltaAbsRank)
    xs.append(tempx)
    ys.append(tempy)

plothandler = plotHandler()
plothandler.drawScatter(xs, ys, 'rank 변화', 'abs(rank) 변화', categories, colors, '각 비디오에 대해서 abs(rank) 변화, rank(변화) scatter(US)', '11usresult.png')