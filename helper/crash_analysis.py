# crash_analysis.py

import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

def run():
    st.subheader("📉 Crash Analysis")

    stock = st.text_input("Enter Stock Symbol (e.g., TSLA)", "TSLA")
    data = yf.download(stock, start="2015-01-01")['Adj Close']

    returns = data.pct_change().dropna()

    fig, ax = plt.subplots()
    ax.plot(data, label="Price")
    ax.set_title(f"{stock} Price Chart")
    st.pyplot(fig)

    drawdown = (data / data.cummax()) - 1
    st.write(f"🔻 Max Drawdown: {drawdown.min():.2%}")
