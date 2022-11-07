import streamlit as st
from custom_functions import *

display_banner()
display_logo()

st.header('CURATED | 🦾 ML 101')

st.markdown("""
### AlphaGo
Before we dive deep into ML/AI it is crucial that we understand the **WHY**s and **WHAT**s of the problems we'll be solving. Reality matters more than theory. 
\n Let's look into the case of `AlphaGo` to understand, what we can do with these capabilities!
""")
embed_yt_video("https://youtu.be/WXuK6gekU1Y")
st.caption("Visit https://www.alphagomovie.com/ for details 😃")

st.markdown("""
___
### MFML - Making Friends With Machine Learning
**Making Friends with Machine Learning**, by [Cassie Kozyrkov](https://twitter.com/quaesita), Chief Decision Scientist, Google is one of the best courses the internet can ever have!
* About Cassie Kozyrkov's work -  https://decision.substack.com/
* Read more about MFML here - https://cloud.google.com/blog/topics/developers-practitioners/ai-all-humans-course-delight-and-inspire

Enjoy the journey! 💡

""")

yt_content_stored('mfml')

st.markdown("""
___
### Consider listening to these podcasts too!
<iframe style="border-radius:12px" src="https://open.spotify.com/embed/episode/2ppGzcN7KjeRRDGafyluDb?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
<iframe style="border-radius:12px" src="https://open.spotify.com/embed/episode/5IaFc479AbjV7u0mh4v1Uy?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
<iframe style="border-radius:12px" src="https://open.spotify.com/embed/episode/3CVF5qpuVMoI12EcXbm04N?utm_source=generator&theme=0" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
<br><br>
""", unsafe_allow_html=True)


goto_page("Take me Home 🏠", "curatED")

footer()