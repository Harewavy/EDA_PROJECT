import streamlit as st
import pandas as pd

# Function to convert columns to appropriate types
def convert_columns(df):
    # Convert 'price' column to numeric, coerce errors
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    # Convert other necessary columns to numeric, coerce errors
    df['model_year'] = pd.to_numeric(df['model_year'], errors='coerce')
    df['cylinders'] = pd.to_numeric(df['cylinders'], errors='coerce')
    df['odometer'] = pd.to_numeric(df['odometer'], errors='coerce')

    return df

# Function to handle missing values
def handle_missing_values(df):
    df['condition'] = df['condition'].fillna('unknown')
    df['fuel'] = df['fuel'].fillna('unknown')
    df['transmission'] = df['transmission'].fillna('unknown')
    df['type'] = df['type'].fillna('unknown')
    df['paint_color'] = df['paint_color'].fillna('unknown')
    df['is_4wd'] = df['is_4wd'].fillna(0).astype(bool)
    return df

# Read the dataset
try:
    df = pd.read_csv('vehicles_us.csv')
except FileNotFoundError:
    st.error("The dataset 'vehicles_us.csv' was not found. Please ensure the file is in the correct location.")
    st.stop()

# Display raw data to inspect column names and data types
st.write("Raw data preview:")
st.write(df.head())

# Clean column names
df.columns = df.columns.str.strip()

# Convert columns to appropriate types
df = convert_columns(df)

# Handle missing values
df = handle_missing_values(df)

# Drop rows with NaN values in 'price'
df = df.dropna(subset=['price'])

# Display cleaned DataFrame preview
st.write("Cleaned DataFrame preview:")
st.write(df.head())

# Check if 'manufacturer' column exists
if 'manufacturer' not in df.columns:
    st.error("The required column 'manufacturer' is missing from the dataset.")
else:
    # Filter manufacturers with more than 1000 ads
    filtered_df = df[df['manufacturer'].map(df['manufacturer'].value_counts()) > 1000]
    st.write("Filtered DataFrame (manufacturers with more than 1000 ads):")

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
