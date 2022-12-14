import streamlit as st
from custom_functions import *

display_banner()
display_logo()

st.header('CURATED | 🧠 THINK BEFORE YOU CODE 💡 ')

col1, col2, col3 = st.columns(3)

with col1:
    with st.expander("What is STRATEGY?", expanded= False ):
        st.markdown("""To many people, **strategy** is a total mystery. But it’s really not complicated, says Harvard Business School’s Felix Oberholzer-Gee, author of "Better, Simpler Strategy". Companies should simplify and focus on two value drivers, he argues: customer satisfaction and employee satisfaction. By aligning strategic initiatives on these alone, leaders make their workers’ jobs less complicated and improve customer experiences. """, unsafe_allow_html=True)
    embed_yt_video("https://www.youtube.com/watch?v=o7Ik1OB4TaE")
with col2:
    with st.expander("A Plan is NOT a Strategy", expanded=False):
        st.markdown("""A comprehensive plan—with goals, initiatives, and budgets–is comforting. But **starting with a plan is a terrible way to make strategy**. Roger Martin, former dean of the Rotman School of Management at the University of Toronto and one of the world’s leading thinkers on strategy, says developing strategy means going outside an organization’s comfort zone and escaping the common traps of strategic planning.""")
    embed_yt_video("https://www.youtube.com/watch?v=iuYlGRnC7J8")
with col3:
    with st.expander("Don't throw away you cumulative Advantage", expanded=False):
        st.markdown("""Brands are constantly changing in order to “stay fresh”, but that’s a mistake. Customers stay loyal through habit, not because you've forced something new and unfamiliar on them. Roger Martin, former dean of the Rotman School of Management at the University of Toronto and one of the world’s leading thinkers on strategy, says brands **shouldn’t be so quick to throw away their cumulative advantage.**""")
    embed_yt_video("https://www.youtube.com/watch?v=dOIRSqNqAzE")


footer()