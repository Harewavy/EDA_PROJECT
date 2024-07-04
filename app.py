import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset
try:
    df = pd.read_csv('vehicles_us.csv')
except FileNotFoundError:
    st.error("The dataset 'vehicles_us.csv' was not found. Please ensure the file is in the correct location.")
    st.stop()

# Display the first few rows for initial debugging
st.write("First few rows of the dataset:")
st.write(df.head())

# Display column names for debugging
st.write("Column names in the dataset:")
st.write(df.columns)

# Check for non-numeric values in the 'price' column
non_numeric_prices = df[~df['price'].astype(str).str.isnumeric()]
if not non_numeric_prices.empty:
    st.error("The 'price' column contains non-numeric values that could not be converted.")
    st.write("Rows with non-numeric 'price' values:")
    st.write(non_numeric_prices)
    st.stop()

# Ensure 'price' column is numeric and handle conversion issues
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Handle any potential NaN values in 'price' after conversion
if df['price'].isnull().any():
    st.error("The 'price' column contains NaN values after conversion.")
    st.write("Rows with NaN values in 'price':")
    st.write(df[df['price'].isnull()])
    st.stop()

# Header
st.header('Car Sales Advertisement Dashboard')

# Check if 'manufacturer' column exists
if 'manufacturer' not in df.columns:
    st.error("The required column 'manufacturer' is missing from the dataset.")
else:
    # Filter manufacturers with more than 1000 ads
    filtered_df = df[df['manufacturer'].map(df['manufacturer'].value_counts()) > 1000]
    st.write("Filtered DataFrame (manufacturers with more than 1000 ads):")
    st.write(filtered_df)

    # Checkbox to show/hide the filtered dataframe
    if st.checkbox('Show Filtered DataFrame'):
        st.write(filtered_df)

    # Plotly Express histogram
    st.header('Price Distribution')
    fig = px.histogram(df, x='price', title='Distribution of Car Prices')
    st.plotly_chart(fig)

    # Plotly Express scatter plot
    st.header('Price vs. Odometer by Condition')
    fig = px.scatter(df, x='odometer', y='price', color='condition', title='Price vs. Odometer by Condition')
    st.plotly_chart(fig)
