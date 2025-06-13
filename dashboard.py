import streamlit as st
import pandas as pd

df = pd.read_csv("patient_data.csv")

st.title("Healthcare Patient Overview Dashboard")
st.write("Dataset Preview", df.head())

st.subheader("Chronic Conditions Distribution")
st.bar_chart(df["ChronicCondition"].value_counts())

st.subheader("Age Distribution")
st.line_chart(df["Age"].value_counts().sort_index())