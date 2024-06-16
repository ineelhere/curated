#for local reference only
from pytube import *

urls = Playlist("https://www.youtube.com/playlist?list=PLqYmG7hTraZDVH599EItlEWsUOsJbAodm")

titles = []
for video_url in urls:
    titles.append(YouTube(video_url).streams[0].title)
details_dict = dict(zip(titles, urls))
print(details_dict)

