import streamlit as st 
from custom_functions import *

display_banner()
display_logo()

st.header('CURATED | 📊 STAT 101')
st.markdown(""" 
Statistics is fundamentally very important if you want to study Machine Learning properly.   

*Quick tip - StatQuest by Josh Starmer is awesome! https://www.youtube.com/@statquest*

Here is a playlist to give you a general overview of statistical concepts.
""",unsafe_allow_html=True)

yt_content_stored('stat_fundamentals')

st.markdown("""
___
Probability is important too. You can refer Sheldon M. Ross: A First Course in Probability

Also there is a fantastic book on Probability and Statistics by Professor Arnab Chakraborty(ISI Kolkata) with the same name

Other than that Khan Academy also provides great resources for Probablity and Statistics.""",unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    embed_yt_video('https://www.youtube.com/watch?v=uhxtUt_-GyM&list=PL1328115D3D8A2566')
with col2:
    embed_yt_video('https://youtu.be/uzkc-qNVoOk')
with col3:
    embed_yt_video('https://www.youtube.com/watch?v=3v9w79NhsfI&list=PLU5aQXLWR3_xDN0M2ZeZ_zHIia0e42_3O')

st.markdown("""
___
Now, let's explore statistical concepts with python.

""",unsafe_allow_html=True)

with st.expander("Statistical Learning with Python - Stanford Online", expanded=False):
    st.markdown("""
    This is an introductory-level course in supervised learning, with a focus on regression and classification methods. The syllabus includes: linear and polynomial regression, logistic regression and linear discriminant analysis; cross-validation and the bootstrap, model selection and regularization methods (ridge and lasso); nonlinear models, splines and generalized additive models; tree-based methods, random forests and boosting; support-vector machines; neural networks and deep learning; survival models; multiple testing. Some unsupervised learning methods are discussed: principal components and clustering (k-means and hierarchical).

    This is not a math-heavy class, so we try and describe the methods without heavy reliance on formulas and complex mathematics. We focus on what we consider to be the important elements of modern data science. Computing is done in Python. There are lectures devoted to Python, giving tutorials from the ground up, and progressing with more detailed sessions that implement the techniques in each chapter.

    The lectures cover all the material in An Introduction to Statistical Learning, with Applications in Python by James, Witten, Hastie, Tibshirani and Taylor (Springer, 2023). The pdf for this book is available for free on the book website.

    What You'll Learn:
    * Overview of statistical learning
    * Linear regression
    * Classification
    * Resampling methods
    * Linear model selection and regularization
    * Moving beyond linearity
    * Tree-based methods
    * Support vector machines
    * Deep learning
    * Survival modeling
    * Unsupervised learning
    * Multiple testing
    """)

yt_content_stored('statpy')

footer()
