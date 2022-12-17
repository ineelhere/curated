import streamlit as st
from streamlit_extras.colored_header import colored_header
from custom_functions import *

st.set_page_config("Curated", "⭐", layout="wide")

display_banner()
display_logo()

colored_header(
    label="Welcome to CURATED 😎",
    description="",
    color_name="blue-70",
)

st.info("**An open source project that focuses on curating awesome resources for learning awesome skills.**")
st.text("\n")

goto_page("Get started with Python 🐍", "Python 101")
goto_page("Understand the WHYs and WHATs of Machine Learning 🦾", "Machine Learning 101")
goto_page("Get started with the concepts in Machine Learning 🤖", "Machine Learning 102")
goto_page("Break into Concepts of Statistics without tears 📊", "Statistics 101")
goto_page("Build cool data apps with Streamlit 🎈", "Streamlit")
goto_page("Build Soft skills to improve the power of your thinking 🧠", "THINK")
goto_page("Provide/receive support with new Opportunities 🎯", "UPLIFT - Job Support")
goto_page("Give Feedback about this project 🤗 ", "Feedback")
goto_page("Collaborate with this project! 🤝 ", "Collaborate!")

st.image("https://media.tenor.com/P2cQctPfjpAAAAAC/im-working-on-it-progress.gif")

footer()
