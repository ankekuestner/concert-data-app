import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Ankes' concert life")


def load_data():
    data = pd.read_csv(r"C:\Users\ankek\Documents\Concert Wrapped\concert-data\concert_sheet.csv", encoding='utf-8', sep=';')
    data = data.rename(columns={'Location Latitude':'latitude', 'Location Longitude':'longitude'})
    return data

data = load_data()

agree = st.checkbox("Show raw data!")
if agree:
    st.write(data)

# Artist information
st.subheader('Artists and Opening Acts')
arr = np.random.normal(1,1, size=100)
fig, ax = plt.subplots()
ax = data['Artist'].value_counts().sort_index(ascending=False).sort_values(ascending=True).plot(kind='barh')
st.pyplot(fig)

# Opening Acts
data['Opening Act'].str.split(";")

arr = np.random.normal(1,1, size=100)
fig, ax = plt.subplots()
ax = data['Opening Act'].value_counts().sort_index(ascending=False).sort_values(ascending=True).plot(kind='barh')
st.pyplot(fig)

# A map of all cities I've been to for concerts
st.subheader('Where have I been for concerts?')
st.map(data=data)

# Search bar to find opening acts for an Artist
artist = st.text_input("Enter the Artist of which you want to know the Opening Act:")
opening_act_list= data.loc[data['Artist'] == artist]['Opening Act'].dropna().unique()
for value in opening_act_list:
    st.write(value)

# Show the total amount of concerts
amount_of_concerts = data['ConcertId'].nunique()
st.metric('Total number of concerts', amount_of_concerts)


