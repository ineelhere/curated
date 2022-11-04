import streamlit as st
from streamlit_extras.app_logo import add_logo
from streamlit_extras.colored_header import colored_header
from custom_functions import *

display_banner()
# add_logo("https://raw.githubusercontent.com/ineelhere/curated/media/media/ic_curated_logo.png")

colored_header(
    label="Welcome to CURATED 😎",
    description="",
    color_name="blue-70",
)

st.info("**An open source project that focuses on curating awesome resources for learning awesome skills.**")
st.text("\n")

goto_page("I want to learn Python 🐍", "Python 101")

st.image("https://media.tenor.com/P2cQctPfjpAAAAAC/im-working-on-it-progress.gif")

footer()