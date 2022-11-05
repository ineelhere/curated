import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.app_logo import add_logo
from pytube import *
from streamlit_player import st_player
import random

def display_banner():
    st.image("https://raw.githubusercontent.com/ineelhere/curated/media/media/ic_curated_banner.png")

def display_logo():
    add_logo(f"https://raw.githubusercontent.com/ineelhere/curated/media/media/ic_curated_logo{random.randint(1,2)}.png")

def goto_page(display_text, destination_page):
    if st.button(display_text):
        switch_page(destination_page)

def get_playlist_video_urls(playlist_url):
    return(Playlist(playlist_url))

def embed_yt_video(video_url):
    st.info(f'**{YouTube(video_url).streams[0].title}**')
    st_player(video_url)
    
def footer():
    st.markdown("""
    ___
    <h3> This work is in progess.</h3>

    [Indraneel Chakraborty](https://www.linkedin.com/in/indraneelchakraborty/) | 2022 | 
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