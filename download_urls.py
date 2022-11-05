#for local use only
from pytube import *

urls = Playlist("https://www.youtube.com/playlist?list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V")

titles = []
for video_url in urls:
    titles.append(YouTube(video_url).streams[0].title)
details_dict = dict(zip(titles, urls))
print(details_dict)