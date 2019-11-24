from handler import DBHandler, plotHandler

config = {
    "host": "localhost",
    "user": "root",
    "password": "ckddud950!",
    "db": "youtube_popular",
}
dbhandler = DBHandler(config)

videoList = dbhandler.getMeaningVideos()
timeIds = dbhandler.getShortTermTimeIds()
x = []
y = []
for video in videoList:
    sql = 'select rank from popular where videoId = "' + video + '" and timeId in' + str(timeIds).replace('[','(').replace(']',')')
    rawRanks = dbhandler.fetchall(sql)
    deltaRank = 0
    deltaAbsRank = 0
    for i in range(0, len(rawRanks) - 1):
        deltaRank += rawRanks[i+1][0] - rawRanks[i][0]
        deltaAbsRank += abs(rawRanks[i+1][0] - rawRanks[i][0])
    if deltaAbsRank < 150:
        x.append(deltaRank)
        y.append(deltaAbsRank)

plothandler = plotHandler()
plothandler.drawScatter(x, y, 'rank', 'abs(rank)', 'blue', '각 비디오에 대해서 abs(rank) 변화, rank(변화) scatter(KR)', '4krresult.png')

config = {
    "host": "localhost",
    "user": "root",
    "password": "ckddud950!",
    "db": "youtube_popular2",
}
dbhandler = DBHandler(config)

videoList = dbhandler.getMeaningVideos()
timeIds = dbhandler.getShortTermTimeIds()
x = []
y = []
for video in videoList:
    sql = 'select rank from popular where videoId = "' + video + '" and timeId in' + str(timeIds).replace('[','(').replace(']',')')
    rawRanks = dbhandler.fetchall(sql)
    deltaRank = 0
    deltaAbsRank = 0
    for i in range(0, len(rawRanks) - 1):
        deltaRank += rawRanks[i+1][0] - rawRanks[i][0]
        deltaAbsRank += abs(rawRanks[i+1][0] - rawRanks[i][0])
    if deltaAbsRank < 150:
        x.append(deltaRank)
        y.append(deltaAbsRank)

plothandler = plotHandler()
plothandler.drawScatter(x, y, 'rank', 'abs(rank)', 'red', '각 비디오에 대해서 abs(rank) 변화, rank(변화) scatter(US)', '4usresult.png')