import streamlit as st
from custom_functions import *

display_banner()
display_logo()

st.header("CURATED | 🎯 UPLIFT")
st.write("""The recent layoffs around the world is unfortunate. \n
**Project CURATED** would like to help the impacted with information regarding open positions ***sourced from social media platforms***.""")

st.warning("**Always ensure the genuine-ness of the opportunity with the organisation/individual before proceeding further.**")

with st.expander("Careerflow's list of companies currently hiring", expanded=False):
    st.markdown("""
    Careerflow provides FREE AI assistant & CRM tools for job seekers. Click  below to view a list of companies hiring directly with Careerflow.

    <a href="https://www.careerflow.ai/still-hiring">https://www.careerflow.ai/still-hiring</a>
    
    Careerflow is checking regularly with companies directly to keep this live list up-to-date.

    Thanks to [Puneet Kohli](https://www.linkedin.com/in/punkohl/), Co-Founder at Careerflow for sharing the info!  🤝

    """,unsafe_allow_html=True)
with st.expander("GrowthX - The Phoenix Project", expanded=False):
    st.markdown("""
    * Main webpage: https://www.growthx.club/phoenix
    * LinkedIn Post: https://www.linkedin.com/posts/abhishpatil_layoffs-are-hard-period-but-the-only-we-activity-6996796748081893376-C_EG
    <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:6996796538110844928" height="1320" width="504" frameborder="0" allowfullscreen="" title="Embedded post"></iframe>
    """, unsafe_allow_html=True)

with st.expander("Streamlit community listings", expanded = False):
    st.markdown("Visit https://discuss.streamlit.io/c/jobs/")

with st.expander("LinkedIn Member Post 1 (Also Check Comments)", expanded=False):
    st.markdown("""
    <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:share:6995396654812065792" height="578" width="504" frameborder="0" allowfullscreen="" title="Embedded post"></iframe>
    """, unsafe_allow_html=True)

with st.expander("LinkedIn Member Post 2 (Also Check Comments)", expanded=False):
    st.markdown("""
    <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:share:6994257805016752128" height="579" width="504" frameborder="0" allowfullscreen="" title="Embedded post"></iframe>
    """, unsafe_allow_html=True)

with st.expander("LinkedIn Member Post 3 (Also Check Comments)", expanded=False):
    st.markdown("""
    <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:share:6996159088808136704" height="1513" width="504" frameborder="0" allowfullscreen="" title="Embedded post"></iframe>
    """, unsafe_allow_html=True)


st.success("""
#### Do you want to Contribute with latest information?
If you are hiring, or know someone who is hiring, please reach out on LinkedIn/Twitter to add the information in this app. DMs are open. \n
* LinkedIn: https://www.linkedin.com/in/indraneelchakraborty/
* Twitter: https://twitter.com/ineelhere
**P.S. Only verified information shall be added.**

""")

footer()