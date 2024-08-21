import streamlit as st
import pandas as pd
import numpy as np

st.title("Ankes' concert life")

@st.cache_data
def load_data():
    data = pd.read_csv(r"C:\Users\ankek\Documents\Concert Wrapped\concert-data\concert_sheet.csv", encoding='unicode_escape', sep=';')
    return data

data = load_data()

agree = st.checkbox("Show raw data!")
if agree:
    st.write(data)