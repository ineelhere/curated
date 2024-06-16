import streamlit as st
from streamlit_extras.colored_header import colored_header
from custom_functions import *

# Set page title and favicon
st.set_page_config("Curated", "⭐", initial_sidebar_state="collapsed")
st.toast('Click on the sidebar to navigate to different pages', icon='👈')
st.toast('Welcome to CURATED!', icon='🎉')

# Display banner and logo
display_banner()
display_logo()

# Colored header
colored_header(
    label="Welcome to CURATED 😎",
    description="An open source project that focuses on curating awesome resources for learning awesome skills.",
    color_name="blue-70",
)

# Introduction text
st.info("**An open source project that focuses on curating awesome resources for learning awesome skills.**")
st.text("\n")

# Define columns for "Go to pages"
col1, col2, col3 = st.columns(3)

# Populate columns with links
with col1:
    goto_page("Get started with Python 🐍", "Python 101")
    goto_page("Understand the WHYs and WHATs of Machine Learning 🦾", "Machine Learning 101")
    goto_page("Get started with the concepts in Machine Learning 🤖", "Machine Learning 102")

with col2:
    goto_page("Break into Concepts of Statistics without tears 📊", "Statistics 101")
    goto_page("Build cool data apps with Streamlit 🎈", "Streamlit")
    goto_page("Build Soft skills to improve the power of your thinking 🧠", "THINK")
    
with col3:
    goto_page("Provide/receive support with new Opportunities 🎯", "UPLIFT - Job Support") 
    
# Display image
st.image("https://media.tenor.com/P2cQctPfjpAAAAAC/im-working-on-it-progress.gif")

goto_page("Give Feedback about this project 🤗 ", "Feedback")
goto_page("Collaborate with this project! 🤝 ", "Collaborate!")

# Footer
footer(0)
