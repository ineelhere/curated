import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.app_logo import add_logo
from streamlit_player import st_player
import random
import pandas as pd
import os
from dotenv import load_dotenv
from datetime import datetime
import pytz
from pymongo import MongoClient
import requests

load_dotenv()
connection_string = os.getenv('DBCS')
db_name = os.getenv('DBNAME')

def display_banner():
    st.image("https://raw.githubusercontent.com/ineelhere/curated/media/media/ic_curated_banner.png")

def display_logo():
    add_logo(f"https://raw.githubusercontent.com/ineelhere/curated/media/media/ic_curated_logo{random.randint(1,5)}.png", height=200)

def goto_page(display_text, destination_page):
    if st.button(display_text):
        switch_page(destination_page)

def embed_yt_video(video_url):
    st_player(video_url)

def yt_content_stored(keyword):
  if keyword == 'mfml':
    videos_dict = download_data(db_name, 'mfml', connection_string)
  elif keyword == 'cs50p':
    videos_dict = download_data(db_name, 'cs50p', connection_string)
  elif keyword == 'mlex':
    videos_dict = download_data(db_name, 'mlex', connection_string)
  elif keyword == 'cs229':
    videos_dict = download_data(db_name, 'cs229', connection_string)
  elif keyword == 'streamlit':
    videos_dict = download_data(db_name, 'streamlit', connection_string)
  elif keyword == 'cs230':
    videos_dict =  download_data(db_name, 'cs230', connection_string)
  elif keyword == 'deepmind_rl':
    videos_dict = download_data(db_name, 'deepmind_rl', connection_string)
  elif keyword == "stat_fundamentals":
    videos_dict = download_data(db_name, 'stat_fundamentals', connection_string)
  elif keyword == "statpy":
    videos_dict = download_data(db_name, 'statpy', connection_string)

  titles_list = videos_dict.keys()
  title_selected = st.selectbox("👇 Select the lecture you want to watch from the dropdown 👇",titles_list)
  if title_selected:
      embed_yt_video(videos_dict.get(title_selected))


def footer(flag=1):
    df = pd.read_json("https://api.quotable.io/random")
    st.write("\n")
    if flag==1:
       goto_page("Take me Home 🏠", "curatED")
    
    st.markdown("""
    ___
    <i>Collaborations are always welcome - https://github.com/ineelhere/curated </i><br>
    <a href="https://www.linkedin.com/in/indraneelchakraborty/" target="_blank">
        <img src="https://img.icons8.com/fluency/48/000000/linkedin.png" width="20" height="20"/>
      </a>[![](https://img.shields.io/github/stars/ineelhere/curated?style=social)](https://github.com/ineelhere/curated) &nbsp; [![](https://img.shields.io/twitter/follow/ineelhere?style=social)](https://twitter.com/ineelhere)""", unsafe_allow_html=True)
    st.info(f"*{df.content[0]}*\n-*{df.author[0]}*")
    visit_count(connection_string, db_name)

def download_data(db_name, collection_name, connection_string):
    """
    Downloads data from MongoDB and returns it as a dictionary.

    :param db_name: Name of the database.
    :param collection_name: Name of the collection.
    :param connection_string: MongoDB connection string.
    :return: Dictionary containing the fetched data.
    """
    client = MongoClient(connection_string)
    db = client[db_name]
    collection = db[collection_name]
    
    # Fetch the data
    documents = collection.find()
    
    # Convert the fetched data into a dictionary
    data_dict = {doc['title']: doc['url'] for doc in documents}
    
    return data_dict

def get_public_ip():
    try:
        response = requests.get('https://httpbin.org/ip')
        response.raise_for_status()
        return response.json()['origin']
    except requests.RequestException as e:
        print(f"Error fetching IP: {e}")
        return 'unknown'

def visit_count(connection_string, db_name):
    utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)
    ist = pytz.timezone('Asia/Kolkata')
    ist_now = utc_now.astimezone(ist)
    
    ip_address = get_public_ip()
    
    client = MongoClient(connection_string)
    db = client[db_name]
    collection = db['visit_count']
    
    document = {
        'ist_time': ist_now.strftime('%d-%B-%Y, %I:%M:%S %p IST'),
        'utc_time': utc_now.strftime('%d-%B-%Y, %I:%M:%S %p UTC'),
        'ip_address': ip_address
    }
    
    collection.insert_one(document)
