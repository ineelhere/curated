import streamlit as st
from custom_functions import *

display_banner()
display_logo()

st.header('CURATED | 🎈 STREAMLIT')

st.info("**This whole project is built on Streamlit 😉**")

st.markdown("""
### Streamlit = A faster way to build and share data apps <br>
Streamlit turns data scripts into shareable web apps in minutes. All in pure Python. No front‑end experience required.
""", unsafe_allow_html=True)

st.video("https://s3-us-west-2.amazonaws.com/assets.streamlit.io/videos/hero-video.mp4")

yt_content_stored('streamlit')

footer()