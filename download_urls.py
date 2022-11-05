#for local reference only
from pytube import *

urls = Playlist("https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU")

titles = []
for video_url in urls:
    titles.append(YouTube(video_url).streams[0].title)
details_dict = dict(zip(titles, urls))
print(details_dict)

# @st.cache()
# def magic(playlist_url):
#     urls = Playlist(playlist_url)
#     titles = []
#     for video_url in urls:
#       titles.append(YouTube(video_url).streams[0].title)
#     details_dict = dict(zip(titles, urls))
#     return(details_dict)

# def yt_content_live(url):
#   videos_dict = magic(url)
#   titles_list = videos_dict.keys()
#   title_selected = st.selectbox("👇 Select the lecture you want to watch from the dropdown 👇",titles_list)
#   if title_selected:
#       embed_yt_video(videos_dict.get(title_selected))