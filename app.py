import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset
df = pd.read_csv('vehicles_us.csv')

# Clean column names
df.columns = df.columns.str.strip()

# Function to convert columns to appropriate types
def convert_columns(df):
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
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

# Convert columns to appropriate types
df = convert_columns(df)

# Handle missing values
df = handle_missing_values(df)

# Drop rows with NaN values in 'price'
df = df.dropna(subset=['price'])

# Check if 'manufacturer' column exists
if 'manufacturer' not in df.columns:
    st.error("The required column 'manufacturer' is missing from the dataset.")
    st.stop()

# Display headers and charts
st.header('Car Sales Advertisement Dashboard')

# Checkbox to show/hide the raw data
if st.checkbox('Show Raw Data'):
    st.write(df.head(10))

# Plotly Express histogram
st.header('Price Distribution')
fig = px.histogram(df, x='price', title='Distribution of Car Prices')
st.plotly_chart(fig)

# Plotly Express scatter plot
st.header('Price vs. Odometer by Condition')
fig = px.scatter(df, x='odometer', y='price', color='condition', title='Price vs. Odometer by Condition')
st.plotly_chart(fig)

# Checkbox to show/hide filtered dataframe
filtered_df = df[df['manufacturer'].map(df['manufacturer'].value_counts()) > 1000]
if st.checkbox('Show Filtered DataFrame (Manufacturers with more than 1000 ads)'):
    st.write(filtered_df)

# Add more visualizations as needed
