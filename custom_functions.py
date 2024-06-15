import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.app_logo import add_logo
from streamlit_player import st_player
import random
from dict_source import *
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
connection_string = os.getenv('DBCS')
db_name = os.getenv('DBNAME')

def display_banner():
    st.image("https://raw.githubusercontent.com/ineelhere/curated/media/media/ic_curated_banner.png")

def display_logo():
    add_logo(f"https://raw.githubusercontent.com/ineelhere/curated/media/media/ic_curated_logo{random.randint(1,5)}.png")

def goto_page(display_text, destination_page):
    if st.button(display_text):
        switch_page(destination_page)

def embed_yt_video(video_url):
    st_player(video_url)

def yt_content_stored(keyword):
  if keyword == 'mfml':
    videos_dict = download_data(db_name, 'mfml', connection_string)
  elif keyword == 'cs50p':
    videos_dict = download_data(db_name, 'cs50p', connection_string)
  elif keyword == 'mlex':
    videos_dict = download_data(db_name, 'mlex', connection_string)
  elif keyword == 'cs229':
    videos_dict = download_data(db_name, 'cs229', connection_string)
  elif keyword == 'streamlit':
    videos_dict = download_data(db_name, 'streamlit', connection_string)
  elif keyword == 'cs230':
    videos_dict =  download_data(db_name, 'cs230', connection_string)
  elif keyword == 'deepmind_rl':
    videos_dict = download_data(db_name, 'deepmind_rl', connection_string)
  elif keyword == "stat_fundamentals":
    videos_dict = download_data(db_name, 'stat_fundamentals', connection_string)

  titles_list = videos_dict.keys()
  title_selected = st.selectbox("👇 Select the lecture you want to watch from the dropdown 👇",titles_list)
  if title_selected:
      embed_yt_video(videos_dict.get(title_selected))


def footer():
    df = pd.read_json("https://api.quotable.io/random")
    st.write("\n")
    goto_page("Take me Home 🏠", "curatED")
    
    st.markdown("""
    ___
    <i>Collaborations are always welcome - https://github.com/ineelhere/curated </i><br>
    <a href="https://www.linkedin.com/in/indraneelchakraborty/" target="_blank">
        <img src="https://img.icons8.com/fluency/48/000000/linkedin.png" width="20" height="20"/>
      </a>[![](https://img.shields.io/github/stars/ineelhere/curated?style=social)](https://github.com/ineelhere/curated) &nbsp; [![](https://img.shields.io/twitter/follow/ineelhere?style=social)](https://twitter.com/ineelhere)""", unsafe_allow_html=True)
    st.info(f"*{df.content[0]}*\n-*{df.author[0]}*")
