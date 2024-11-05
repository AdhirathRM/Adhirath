import streamlit as st
import seaborn as sns 
import plotly.express as px
import pandas as pd

st.title("Plotly and Streamlit Interactive Visualizations")

st.markdown("<h5 style='color: teal;'>Created by:</h6>", unsafe_allow_html=True)
st.markdown("<p style='color: white;'>1. Adhirath Rajesh Menon </p>", unsafe_allow_html=True)


tips = sns.load_dataset('tips')  # Loading the dataset
print(tips.head())  # This will show the first 5 rows of the tips dataset

st.subheader("Task 2: Bar Chart")

fig2 = px.bar(
    tips, x='day', y='tip', color='day',
    title='Average Tip by Day',
    labels={'tip': 'Average Tip ($)', 'day': 'Day of the Week'},
    template='plotly_white',  # Clean white background
)
fig2.show()
st.plotly_chart(fig2)

fig4 = px.scatter(
    tips, x='total_bill', y='tip', color='sex',
    title='Total Bill vs Tip (Colored by Gender)',
    labels={'total_bill': 'Total Bill ($)', 'tip': 'Tip ($)'},
    template='plotly_dark',  # Using a cool dark theme
    size='size'  # The size of points based on the size of the group
)
fig4.show()