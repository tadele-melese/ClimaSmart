import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run_dashboard():
    st.title("ClimaSmart Drought Index Explorer")

    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, index_col=0, parse_dates=True)
        index_name = st.selectbox("Select Index Column", df.columns)

        st.line_chart(df[index_name])

        threshold = st.slider("Drought Threshold", min_value=-3.0, max_value=0.0, value=-1.0)
        drought_events = df[df[index_name] < threshold]
        st.write(f"⚠️ {len(drought_events)} drought points below threshold.")
