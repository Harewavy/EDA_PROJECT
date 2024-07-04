import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')
df.columns = df.columns.str.strip()
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0] if pd.notnull(x) else x)

def convert_columns(df):
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['model_year'] = pd.to_numeric(df['model_year'], errors='coerce')
    df['cylinders'] = pd.to_numeric(df['cylinders'], errors='coerce')
    df['odometer'] = pd.to_numeric(df['odometer'], errors='coerce')
    return df

def handle_missing_values(df):
    df['condition'] = df['condition'].fillna('unknown')
    df['fuel'] = df['fuel'].fillna('unknown')
    df['transmission'] = df['transmission'].fillna('unknown')
    df['type'] = df['type'].fillna('unknown')
    df['paint_color'] = df['paint_color'].fillna('unknown')
    df['is_4wd'] = df['is_4wd'].fillna(0).astype(bool)
    return df

df = convert_columns(df)
df = handle_missing_values(df)
df = df.dropna(subset=['price'])

if 'manufacturer' not in df.columns:
    st.error("The required column 'manufacturer' is missing from the dataset.")
    st.stop()

st.header('Car Sales Advertisement Dashboard')

if st.checkbox('Show Raw Data'):
    st.write(df.head(10))

st.header('Price Distribution')
fig = px.histogram(df, x='price', title='Distribution of Car Prices')
st.plotly_chart(fig)

st.header('Price vs. Odometer by Condition')
fig = px.scatter(df, x='odometer', y='price', color='condition', title='Price vs. Odometer by Condition')
st.plotly_chart(fig)

filtered_df = df[df['manufacturer'].map(df['manufacturer'].value_counts()) > 1000]
if st.checkbox('Show Filtered DataFrame (Manufacturers with more than 1000 ads)'):
    st.write(filtered_df)


