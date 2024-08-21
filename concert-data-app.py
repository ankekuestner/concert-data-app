import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Ankes' concert life")

@st.cache_data
def load_data():
    data = pd.read_csv(r"C:\Users\ankek\Documents\Concert Wrapped\concert-data\concert_sheet.csv", encoding='unicode_escape', sep=';')
    return data

data = load_data()

agree = st.checkbox("Show raw data!")
if agree:
    st.write(data)

# Artist information
st.subheader('Artist information')
st.write(data['Artist'].value_counts())
arr = np.random.normal(1,1, size=100)
fig, ax = plt.subplots()
ax = data['Artist'].value_counts().sort_index(ascending=False).sort_values(ascending=True).plot(kind='barh')
st.pyplot(fig)

arr = np.random.normal(1,1, size=100)
fig, ax = plt.subplots()
ax = data['Opening Act'].value_counts().sort_index(ascending=False).sort_values(ascending=True).plot(kind='barh')
st.pyplot(fig)