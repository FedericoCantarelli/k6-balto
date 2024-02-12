import streamlit as st
from k6_malinois import k6_malinois
import pandas as pd
import datetime

st.set_page_config(
    page_title="General Overview",
    page_icon="🐕‍🦺",
)

st.write("# Welcome to K6 Malinois! 🐕‍🦺")
st.write("👋 Hi, welcome to K& Malinois.")

st.markdown(
    """
    
K6 Malinois is a dashboard that allows you to analyze and visualize the data 
obtained using K6 by Grafana to perform load testing of APIs. On this page, you will find a 
general overview of the results. In the "Chart detail" section, you will find a more detailed 
description of the result, while on the "Statistics" page, 
you will find useful statistics to better understand the system's performance.
"""
)
st.sidebar.header("General Overview")
uploaded_file = st.sidebar.file_uploader("Upload K6 output", "csv")
st.write("## Dataframe")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  df["timestamp"] = df.timestamp.apply(lambda ts: datetime.datetime.fromtimestamp(ts, datetime.UTC).strftime("%Y-%m-%d %H:%M:%S"))
  st.dataframe(df)
  st.session_state.df = df
else:
  st.error("🛑 Import K6 output using the widget in the sidebar.")