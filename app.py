import streamlit as st
import pandas as pd

# Read the dataset
try:
    df = pd.read_csv('vehicles_us.csv')
except FileNotFoundError:
    st.error("The dataset 'vehicles_us.csv' was not found. Please ensure the file is in the correct location.")
    st.stop()

# Display raw data to inspect column names and data types
st.write("Raw data preview:")
st.write(df.head())

# Ensure 'price' column is numeric and handle conversion issues
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Drop rows with NaN values in 'price'
df = df.dropna(subset=['price'])

# Display cleaned 'price' column
st.write("Cleaned 'price' column preview:")
st.write(df['price'].head(10))

# Display cleaned DataFrame preview
st.write("Cleaned DataFrame preview:")
st.write(df.head())
