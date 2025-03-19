import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('../data/smart_home_energy_consumption_large.csv')
st.title("Energy Consumption Analysis")
fig = px.bar(df, x='Appliance Type', y='Energy Consumption (kWh)')
st.plotly_chart(fig)
