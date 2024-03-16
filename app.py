# app.py
import streamlit as st
from tiktok_data_collector import collect_tiktok_data
from data_processor import process_data
from visualization import create_visualization
import pandas as pd

# Set the title of the dashboard
st.title('TikTok Analytics Dashboard')

# Sidebar for user inputs
st.sidebar.header('User Input Features')
selected_hashtag = st.sidebar.text_input('Hashtag', value='dance')

# Collect and process data based on the input hashtag
raw_data = collect_tiktok_data(hashtag=selected_hashtag)
processed_data = process_data(raw_data)

# Placeholder for visualization
# This should be replaced by calls to the visualization functions
st.write("Data visualization will appear here.")

# Displaying the data in a table
st.write(processed_data)

# Run this with `streamlit run app.py` from the command line to start the web server and serve the dashboard.

