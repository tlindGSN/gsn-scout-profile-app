import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="GSN SCOUT Profile", layout="wide")

st.image("GSN_logo_300dpi_CMYK.png", width=200)
st.title("GSN SCOUT Business Profile Generator")

uploaded_file = st.file_uploader("Upload CSV with Team Assessment Data", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file, index_col=0)
    st.subheader("Uploaded Data")
    st.dataframe(df)

    means = df.mean()
    stds = df.std(ddof=0)
    z_scores = (df - means) / stds

    st.subheader("Mean Trait Scores")
    st.bar_chart(means)

    st.subheader("Z-Score Profile (Team)")
    st.line_chart(z_scores)

    st.subheader("Radar Chart (Mean Scores)")
    fig = px.line_polar(r=df.T, theta=df.columns, line_close=True)
    st.plotly_chart(fig)
