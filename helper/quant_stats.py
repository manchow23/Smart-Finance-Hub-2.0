# quant_stats.py

import streamlit as st
import yfinance as yf
import pandas as pd

def run():
    st.subheader("📐 Quantitative Insights")

    ticker = st.text_input("Enter Stock Symbol", "TSLA")
    data = yf.download(ticker, start="2018-01-01")['Adj Close']
    returns = data.pct_change().dropna()

    st.write("📊 Descriptive Statistics")
    st.write(returns.describe())

    st.write("🔁 Rolling Mean (50-day)")
    st.line_chart(data.rolling(50).mean())
