"""Main module."""
import streamlit as st
import pandas as pd
import datetime
def read_file(file: st.runtime.uploaded_file_manager.UploadedFile) -> pd.DataFrame:
    df = pd.read_csv(file)
    df["timestamp"] = df.timestamp.apply(lambda ts: datetime.datetime.fromtimestamp(ts, datetime.UTC).strftime("%Y-%m-%d %H:%M:%S"))
    return df
