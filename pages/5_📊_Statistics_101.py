import streamlit as st 
from custom_functions import *

display_banner()
display_logo()

st.header('CURATED | 📊 STAT 101')
st.markdown(""" 
Statistics is fundamentally very important if you want to study Machine Learning properly.   

*Quick tip - StatQuest by Josh Starmer is awesome! https://www.youtube.com/@statquest*

Here is a playlist to give you a general overview of statistical concepts.
""",unsafe_allow_html=True)

yt_content_stored('stat_fundamentals')

st.markdown("""
___
Probability is important too. You can refer Sheldon M. Ross: A First Course in Probability

Also there is a fantastic book on Probability and Statistics by Professor Arnab Chakraborty(ISI Kolkata) with the same name

Other than that Khan Academy also provides great resources for Probablity and Statistics.""",unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    embed_yt_video('https://www.youtube.com/watch?v=uhxtUt_-GyM&list=PL1328115D3D8A2566')
with col2:
    embed_yt_video('https://youtu.be/uzkc-qNVoOk')
with col3:
    embed_yt_video('https://www.youtube.com/watch?v=3v9w79NhsfI&list=PLU5aQXLWR3_xDN0M2ZeZ_zHIia0e42_3O')

footer()
