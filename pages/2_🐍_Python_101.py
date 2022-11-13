import streamlit as st
from custom_functions import *

display_banner()
display_logo()

st.header('CURATED | 🐍 PYTHON 101')

st.markdown("""
If this is your first time learning Python (or maybe you're here to revise concepts), Harvard University's `CS50’s Introduction to Programming with Python` is one of the best resources available on the internet.

Here are some additional resources you might wish to checkout -
* Visit the python documentation (v3.X) - https://docs.python.org/3/
* Visit the Official CS50 Website - https://cs50.harvard.edu/python/2022/
* About Prof David J. Malan - https://cs.harvard.edu/malan/

Go ahead and binge watch the videos! 😉
___
""")

yt_content_stored("cs50p")



footer()