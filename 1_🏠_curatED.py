import streamlit as st
from streamlit_extras.app_logo import add_logo
from streamlit_extras.colored_header import colored_header
from custom_functions import *

display_banner()
add_logo("https://raw.githubusercontent.com/ineelhere/curated/media/media/ic_curated_logo.png")

colored_header(
    label="Welcome to CURATED 😎",
    description="",
    color_name="blue-70",
)

st.info("**An open source project that focuses on curating awesome resources for learning awesome skills.**")
st.text("\n")

goto_page("I want to learn Python 🐍", "Python 101")

st.image("https://harmony.imgix.net/https%3A%2F%2Fcollectiveidea.harmonycms.com%2Fassets%2Ffangirl.gif?auto=compress&s=ecc5cf01f62905da19ccca763481d747")