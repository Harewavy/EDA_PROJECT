import streamlit as st
import pandas as pd

# Read the dataset
try:
    df = pd.read_csv('vehicles_us.csv')
except FileNotFoundError:
    st.error("The dataset 'vehicles_us.csv' was not found. Please ensure the file is in the correct location.")
    st.stop()

# Display initial data info for the 'price' column
st.write("Initial data info for the 'price' column:")
st.write(df['price'].head(10))

# Check for non-numeric values in the 'price' column
non_numeric_prices = df[~df['price'].astype(str).str.isnumeric()]
if not non_numeric_prices.empty:
    st.error("The 'price' column contains non-numeric values that could not be converted.")
    st.write("Rows with non-numeric 'price' values:")
    st.write(non_numeric_prices)
    st.stop()

# Ensure 'price' column is numeric and handle conversion issues
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Check if there are any NaN values in 'price' after conversion
if df['price'].isnull().any():
    st.write("Rows with NaN values in 'price' after conversion:")
    st.write(df[df['price'].isnull()])
    # Drop rows with NaN values in 'price'
    df = df.dropna(subset=['price'])

# Display the cleaned 'price' column
st.write("Cleaned 'price' column:")
st.write(df['price'].head(10))

# Display first 10 rows of the dataframe to confirm 'price' column is clean
st.write("First 10 rows of the cleaned dataframe:")
st.write(df.head(10))
