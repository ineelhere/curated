import streamlit as st
from custom_functions import *

display_banner()
display_logo()

st.header('CURATED | 🐍 PYTHON 101')

st.markdown("""
### Git it Right!
So, before you start to code, it is very important you understand how to maintain code. \n
Just like you keep a log of your tasks somewhere like a diary or a to do checklist, it is important to track the changes you made to your code since the very beginning of a project. That, we can do with `git`! \n
""", unsafe_allow_html=True)
st.info("**Cool fact**: This whole project has been version controlled with Git on GitHub! \n Visit https://github.com/ineelhere/curated")
st.write("First, watch this video. Dr Max Wilson, from the University of Nottingham, gives us an overview.")

col1, col2 = st.columns(2)

with col1:
    embed_yt_video("https://www.youtube.com/watch?v=92sycL8ij-U")
with col2:
    embed_yt_video("https://www.youtube.com/watch?v=bSA91XTzeuA")
   
st.write("Now, let's understand some more about `git` from Harvard University's CS50W")
embed_yt_video("https://www.youtube.com/watch?v=NcoBAfJ6l2Q")

st.markdown("""
### Okay, let's now dive in to Python!
If this is your first time learning Python (or maybe you're here to revise concepts), Harvard University's `CS50’s Introduction to Programming with Python` is one of the best resources available on the internet.

Here are some additional resources you might wish to checkout -
* Visit the python documentation (v3.X) - https://docs.python.org/3/
* Visit the Official CS50 Website - https://cs50.harvard.edu/python/2022/
* About Prof David J. Malan - https://cs.harvard.edu/malan/

Go ahead and binge watch the videos! 😉
""")

yt_content_stored("cs50p")



footer()