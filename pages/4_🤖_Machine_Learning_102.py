import streamlit as st
from custom_functions import *

display_banner()
display_logo()

st.header('CURATED | 🤖 ML 102')

st.markdown("""
___
### Introduction or Revision
Take these short courses on Kaggle 
- https://www.kaggle.com/learn/pandas : **Pandas** - Solve short hands-on challenges to perfect your data manipulation skills.
- https://www.kaggle.com/learn/data-cleaning : **Data Cleaning** - Master efficient workflows for cleaning real-world, messy data.
- https://www.kaggle.com/learn/data-visualization : **Data Visualization** - Make great data visualizations. A great way to see the power of coding!
- https://www.kaggle.com/learn/intro-to-machine-learning : **Intro to Machine Learning** - Learn the core ideas in machine learning, and build your first models.
""")


st.markdown("""
___
Okay, now hear this!
""")
embed_yt_video("https://youtu.be/yrtAoBr3iuQ")

st.markdown("""
____
### Let's dive deeper now!
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

goto_page("Take me Home 🏠", "curatED")

footer()