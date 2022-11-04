import streamlit as st
from custom_functions import *

display_banner()

st.header('CURATED | 🐍 PYTHON 101')

st.markdown("""
If this is your first time learning Python (or maybe you're here to revise concepts), Harvard University's `CS50’s Introduction to Programming with Python` is one of the best resources available on the internet.

Here are some additional resources you might wish to checkout -
* Visit the python documentation (v3.X) - https://docs.python.org/3/
* Visit the Official CS50 Website - https://cs50.harvard.edu/python/2022/
* About Prof David J. Malan - https://cs.harvard.edu/malan/

Go ahead and binge watch the videos! 😉
""")

urls_list = get_playlist_video_urls("https://www.youtube.com/playlist?list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V")
for i in urls_list:
    embed_yt_video(i)
    
goto_page("Go to the beginning 🐍", "Python 101")

footer()