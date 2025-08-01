
import streamlit as st
import pandas as pd

st.title("Customer Churn Dashboard")

df = pd.read_csv('../../data/customer_churn.csv')
st.write("Data Preview", df.head())

st.bar_chart(df['Churn'].value_counts())
