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
Okay, first hear these!
""")

col1, col2, col3 = st.columns(3)

with col2:
    embed_yt_video("https://www.youtube.com/watch?v=I2ZK3ngNvvI")
with col3:
    embed_yt_video("https://youtu.be/yrtAoBr3iuQ")
with col1:
    embed_yt_video("https://www.youtube.com/watch?v=1k37OcjH7BM")


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


st.markdown("""
___
### Deep Learning - CS230

Lectures from Stanford graduate course CS230 taught by [Andrew Ng](https://www.andrewng.org/).

You will learn about Convolutional networks, RNNs, LSTM, Adam, Dropout, BatchNorm, Xavier/He initialization, and more.

You will work on case studies from healthcare, autonomous driving, sign language reading, music generation, and natural language processing. You will master not only the theory, but also see how it is applied in industry. You will practice all these ideas in Python and in TensorFlow, which we will teach.

For more information about Stanford's Artificial Intelligence professional and graduate programs, visit: https://stanford.io/ai
""")

yt_content_stored('cs230')


st.markdown("""
___
### DeepMind x UCL | Reinforcement Learning Lecture Series 2021
The Reinforcement Learning Lecture Series is a collaboration between DeepMind and the UCL Centre for Artificial Intelligence.
""")

yt_content_stored('deepmind_rl')
footer()