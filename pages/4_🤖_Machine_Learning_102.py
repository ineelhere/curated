import streamlit as st
from custom_functions import *

display_banner()
display_logo()

st.header('CURATED | 🤖 ML 102')

st.markdown("""
Led by [Andrew Ng](https://www.andrewng.org/), this course provides a broad introduction to machine learning and statistical pattern recognition. 

Topics include: 
- supervised learning (generative/discriminative learning 
- parametric/non-parametric learning 
- neural networks, support vector machines)
- unsupervised learning (clustering, dimensionality reduction, kernel methods)
- learning theory (bias/variance tradeoffs, practical advice)
- reinforcement learning and adaptive control. 

The course will also discuss recent applications of machine learning, such as to robotic control, data mining, autonomous navigation, bioinformatics, speech recognition, and text and web data processing.

""")
yt_content_stored('cs229')