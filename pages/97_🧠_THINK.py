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

col1, col2, col3 = st.columns(3)

with col1:
    with st.expander("Mental Strength!", expanded= False ):
        st.markdown("""First, **realize there’s a difference between acting tough and actually being mentally strong**. \nDeveloping mental strength takes practice, and involves overcoming our natural anxieties so we can handle difficult situations. Amy Morin, author of “13 Things Mentally Strong People Don't Do”, says it’s not about making sure you never fail, but telling yourself that you are strong enough to deal with failure when it inevitably happens.""", unsafe_allow_html=True)
    embed_yt_video("https://www.youtube.com/watch?v=rxDjTyWRqDA")
with col2:
    with st.expander("How and When to Disrupt Your Career, and Yourself (Quick Study)", expanded=False):
        st.markdown("""If you’re comfortable but bored at your current position, you’re in the danger zone. Here are some ways to keep growing without leaving your company. \nWhitney Johnson, an executive coach and author of "Disrupt Yourself", says we give a lot of airtime to building disruptive products and services, to buying and/or investing in disruptive companies, and we should. Both are vital engines of economic growth. But, the most overlooked engine of growth is the individual. If you are really looking to move the world forward, begin by innovating on the inside, and disrupt yourself.""")
    embed_yt_video("https://www.youtube.com/watch?v=1wrQ6Msp7wM")
with col3:
    with st.expander("Your Career Path Doesn't Have to Be a Straight Line", expanded=False):
        st.markdown("""You may think of your career as a ladder–you can go up, or down–but a better analogy might be a rock climbing wall, where going sideways, or even backwards, can be how you find your unique route to the top. KeyAnna Schmiedl, global head of culture and inclusion at Wayfair, explains what real-life rock climbing taught her about defining career advancement for herself.""")
    embed_yt_video("https://www.youtube.com/watch?v=oAgMKap9Cv8")

footer()