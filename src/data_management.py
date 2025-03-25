import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache_data
def load_airplane_data():
    df = pd.read_csv("outputs/datasets/collection/airplane_performance_study.csv")
    return df


def load_pkl_file(file_path):  # Have not modified this code!
    return joblib.load(filename=file_path)  # Have not modified this code!
