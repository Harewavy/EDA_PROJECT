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

# Display the data types of each column
st.write("Data types of each column:")
st.write(df.dtypes)

# Convert all columns to appropriate data types
# Ensure 'price' column is numeric and handle conversion issues
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Check if there are any NaN values in 'price' after conversion
if df['price'].isnull().any():
    st.write("Rows with NaN values in 'price' after conversion:")
    st.write(df[df['price'].isnull()])
    # Fill NaN values with 0 or drop rows with NaN values in 'price'
    df = df.dropna(subset=['price'])

# Display the cleaned data types of each column
st.write("Cleaned data types of each column:")
st.write(df.dtypes)

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
