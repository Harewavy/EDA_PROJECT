import streamlit as st
import pandas as pd
import numpy as np

# Function to display detailed data information
def display_data_info(df):
    st.write("First few rows of the dataset:")
    st.write(df.head())
    st.write("Column names in the dataset:")
    st.write(df.columns)
    st.write("Data types of each column:")
    st.write(df.dtypes)
    st.write("Summary statistics of the dataset:")
    st.write(df.describe(include='all'))

# Function to clean data
def clean_data(df):
    # Ensure 'price' column is numeric and handle conversion issues
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    # Drop rows with NaN values in 'price'
    df = df.dropna(subset=['price'])

    # Ensure all columns have the correct data types
    df['model_year'] = pd.to_numeric(df['model_year'], errors='coerce')
    df['cylinders'] = pd.to_numeric(df['cylinders'], errors='coerce')
    df['odometer'] = pd.to_numeric(df['odometer'], errors='coerce')

    # Ensure 'is_4wd' column is boolean
    df['is_4wd'] = df['is_4wd'].astype('bool', errors='ignore')

    # Fill NaN values in non-numeric columns with a placeholder
    df['condition'] = df['condition'].fillna('unknown')
    df['fuel'] = df['fuel'].fillna('unknown')
    df['transmission'] = df['transmission'].fillna('unknown')
    df['type'] = df['type'].fillna('unknown')
    df['paint_color'] = df['paint_color'].fillna('unknown')

    return df

# Read the dataset
try:
    df = pd.read_csv('vehicles_us.csv')
except FileNotFoundError:
    st.error("The dataset 'vehicles_us.csv' was not found. Please ensure the file is in the correct location.")
    st.stop()

# Clean the dataset
df = clean_data(df)

# Display initial data info
st.write("Data before display:")
st.write(df.head(10))  # Display the first 10 rows for better visibility

# Display the cleaned data info
display_data_info(df)

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
