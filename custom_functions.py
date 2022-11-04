import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from pytube import *
from streamlit_player import st_player

def display_banner():
    st.image("https://raw.githubusercontent.com/ineelhere/curated/media/media/ic_curated_banner.png")

def goto_page(display_text, destination_page):
    if st.button(display_text):
        switch_page(destination_page)

def get_playlist_video_urls(playlist_url):
    return(Playlist(playlist_url))

def embed_yt_video(video_url):
    st.info(f'**{YouTube(video_url).streams[0].title}**')
    st_player(video_url)
    
