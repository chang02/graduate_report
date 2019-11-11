from handler import Handler

config = {
    "host": "localhost",
    "user": "root",
    "password": "ckddud950!",
    "db": "youtube_popular",
}
handler = Handler(config)
print(handler.getTimeIds(1))