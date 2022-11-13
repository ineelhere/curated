import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.app_logo import add_logo
from streamlit_player import st_player
import random
from dict_source import *

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
    videos_dict = mfml_dict()
  elif keyword == 'cs50p':
    videos_dict = cs50p()
  elif keyword == 'mlex':
    videos_dict = mlex()
  elif keyword == 'cs229':
    videos_dict = cs229_dict()
  elif keyword == 'streamlit':
    videos_dict = streamlit()  
  titles_list = videos_dict.keys()
  title_selected = st.selectbox("👇 Select the lecture you want to watch from the dropdown 👇",titles_list)
  if title_selected:
      embed_yt_video(videos_dict.get(title_selected))


def footer():
    st.write("\n")
    goto_page("Take me Home 🏠", "curatED")
    st.markdown("""
    ___
    <i>Collaborations are always welcome - https://github.com/ineelhere/curated </i><br>
    Developer Info: <a href="https://www.linkedin.com/in/indraneelchakraborty/" target="_blank"> Indraneel Chakraborty </a> | 2022 | 
      <a href="https://www.linkedin.com/in/indraneelchakraborty/" target="_blank">
        <img src="https://img.icons8.com/fluency/48/000000/linkedin.png" width="20" height="20"/>
      </a>
      <a href="https://twitter.com/ineelhere" target="_blank">
        <img src="https://abs.twimg.com/favicons/twitter.ico" alt="Twitter" width="20" height="20">
      </a>
      <a href="https://www.youtube.com/channel/UCbIMzl7rOj0FkamVf_aBM8w" target="_blank">
        <img src="https://www.youtube.com/s/desktop/28b67e7f/img/favicon_48.png" alt="YouTube" width="20" height="20">
      </a>
      <a href="https://github.com/ineelhere" target="_blank">
        <img width="20" height="20" src="https://github.com/fluidicon.png" alt="Github">
      </a>
    </div>
    </section>
    </main>    """, unsafe_allow_html=True)