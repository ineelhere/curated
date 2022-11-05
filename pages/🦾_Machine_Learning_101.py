import streamlit as st
from custom_functions import *

display_banner()
display_logo()

st.header('CURATED | 🦾 ML 101')

st.markdown("""
**Making Friends with Machine Learning**, by [Cassie Kozyrkov](https://twitter.com/quaesita), Chief Decision Scientist, Google is one of the best courses the internet can ever have!
* About Cassie Kozyrkov's work -  https://decision.substack.com/
* Read more about MFML here - https://cloud.google.com/blog/topics/developers-practitioners/ai-all-humans-course-delight-and-inspire

Enjoy the journey! 💡
___
""")

yt_content("https://www.youtube.com/playlist?list=PLRKtJ4IpxJpDxl0NTvNYQWKCYzHNuy2xG")

st.markdown("""
Consider listening to this podcast too!
<iframe style="border-radius:12px" src="https://open.spotify.com/embed/episode/3CVF5qpuVMoI12EcXbm04N?utm_source=generator&theme=0" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
""", unsafe_allow_html=True)

goto_page("Take me Home 🏠", "curatED")

footer()