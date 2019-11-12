from handler import DBHandler, plotHandler

config = {
    "host": "localhost",
    "user": "root",
    "password": "ckddud950!",
    "db": "youtube_popular2",
}
dbhandler = DBHandler(config)

sql = 'select videoId, timeId from popular where rank = 1'
result = dbhandler.fetchall(sql)
views = []
for element in result:
    sql = 'select views from video where videoId = "' + element[0] + '" and timeId = ' + str(element[1])
    result = dbhandler.fetchone(sql)
    if result == None or result[0] == None:
        pass
    else:
        views.append(result[0])

plothandler = plotHandler()
plothandler.drawBox(views, 'views', '특정 인기 순위(1위)에서의 조회수에 대한 boxplot(KR)', '5-3usresult.png')