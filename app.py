import streamlit as st
import pandas as pd
import plotly.express as px

try:
    df = pd.read_csv('vehicles_us.csv')
except FileNotFoundError:
    st.error("The dataset 'vehicles_us.csv' was not found. Please ensure the file is in the correct location.")
    st.stop()

st.write("Data Types and Missing Values in Each Column:")
st.write(df.info())

df['price'] = pd.to_numeric(df['price'], errors='coerce')

if df['price'].isnull().any():
    st.error("The 'price' column contains non-numeric values that could not be converted.")
    st.write("Rows with conversion issues:")
    st.write(df[df['price'].isnull()])
    st.stop()

st.header('Car Sales Advertisement Dashboard')

st.write("First few rows of the dataset:")
st.write(df.head())

st.write("Column names in the dataset:")
st.write(df.columns)

if 'manufacturer' not in df.columns:
    st.error("The required column 'manufacturer' is missing from the dataset.")
else:
    filtered_df = df[df['manufacturer'].map(df['manufacturer'].value_counts()) > 1000]
    st.write("Filtered DataFrame (manufacturers with more than 1000 ads):")
    st.write(filtered_df)

    if st.checkbox('Show Filtered DataFrame'):
        st.write(filtered_df)

    st.header('Price Distribution')
    fig = px.histogram(df, x='price', title='Distribution of Car Prices')
    st.plotly_chart(fig)

    st.header('Price vs. Odometer by Condition')
    fig = px.scatter(df, x='odometer', y='price', color='condition', title='Price vs. Odometer by Condition')
    st.plotly_chart(fig)
