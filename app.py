import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header("Data Viewer")
include_less_than_1000 = st.checkbox('Include manufacturers with less than 1000 ads')

if include_less_than_1000:
    st.write(df)
else:
    filtered_df = df[df['manufacturer'].map(df['manufacturer'].value_counts()) >= 1000]
    st.write(filtered_df)

st.header("Vehicle types by manufacturer")
fig = px.histogram(df, x='manufacturer', color='type', barmode='stack')
st.plotly_chart(fig)

st.header("Histogram of condition vs model year")
fig = px.histogram(df, x='model_year', color='condition', nbins=50)
st.plotly_chart(fig)

st.header("Compare price distribution between manufacturers")
manufacturer1 = st.selectbox('Select manufacturer 1', df['manufacturer'].unique())
manufacturer2 = st.selectbox('Select manufacturer 2', df['manufacturer'].unique())

normalize_hist = st.checkbox('Normalize histogram')

df_manufacturer1 = df[df['manufacturer'] == manufacturer1]
df_manufacturer2 = df[df['manufacturer'] == manufacturer2]

fig = px.histogram(df, x='price', color='manufacturer', nbins=50, barmode='overlay',
                   histnorm='percent' if normalize_hist else None)
st.plotly_chart(fig)
