import streamlit as st 
from custom_functions import *

display_banner()
display_logo()

st.header('CURATED | 📊 STAT 101')
st.markdown(""" 
Statistics is fundamentally very important if you wnat to study Machine Learning. There are multiple sources from which you can study Stat.\n
We shall provide some sources here.\n            
""",unsafe_allow_html=True)

st.write("You can follow the youtube channel StatQuest by Josh Starmer.")
embed_yt_video('https://www.youtube.com/@statquest')

st.markdown("""Probability is important too. You can refer Sheldon M. Ross: A First Course in Probability\n
            Also there is a fantastic book on Probability and Statistics by Professor Arnab Chakraborty(ISI Kolkata) with the same name\n
            Other than that Khan Academy also provides great resources for Probablity and Statistics.
            """,unsafe_allow_html=True)
embed_yt_video('https://www.youtube.com/watch?v=uhxtUt_-GyM&list=PL1328115D3D8A2566')
embed_yt_video('https://www.youtube.com/watch?v=uzkc-qNVoOk&list=PLC58778F28211FA19')

st.write("Random Variable and Probability Distributions")
embed_yt_video('https://www.youtube.com/watch?v=3v9w79NhsfI&list=PLU5aQXLWR3_xDN0M2ZeZ_zHIia0e42_3O')

footer()
