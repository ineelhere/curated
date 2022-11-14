import streamlit as st
from custom_functions import *

display_banner()
display_logo()

st.header('CURATED | YOUR FEEDBACK 🤝 ')

st.markdown('''
<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSd0bw-AmPp0zStQntquZ6I1Ig30B5ShPi0QoWock-lf5GorCQ/viewform?embedded=true" width="640" height="2197" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
''', unsafe_allow_html=True)



footer()