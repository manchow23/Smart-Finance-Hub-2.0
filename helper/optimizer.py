# optimizer.py

import streamlit as st
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.subheader("📈 Portfolio Optimizer")
    tickers = st.text_input("Enter comma-separated tickers", "AAPL, MSFT, GOOGL").split(",")

    data = yf.download(tickers, start="2020-01-01")['Adj Close']
    returns = data.pct_change().dropna()

    num_portfolios = 5000
    all_weights = np.zeros((num_portfolios, len(tickers)))
    ret_arr = np.zeros(num_portfolios)
    vol_arr = np.zeros(num_portfolios)
    sharpe_arr = np.zeros(num_portfolios)

    for i in range(num_portfolios):
        weights = np.random.random(len(tickers))
        weights /= np.sum(weights)
        all_weights[i,:] = weights
        ret_arr[i] = np.sum(returns.mean() * weights * 252)
        vol_arr[i] = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
        sharpe_arr[i] = ret_arr[i]/vol_arr[i]

    max_sharpe_idx = sharpe_arr.argmax()
    best_weights = all_weights[max_sharpe_idx]

    st.write("📌 Best Portfolio Weights:")
    for i, ticker in enumerate(tickers):
        st.write(f"{ticker.strip()}: {best_weights[i]*100:.2f}%")

    fig, ax = plt.subplots()
    scatter = ax.scatter(vol_arr, ret_arr, c=sharpe_arr, cmap='plasma')
    ax.scatter(vol_arr[max_sharpe_idx], ret_arr[max_sharpe_idx], c='red', s=50)
    ax.set_xlabel("Volatility")
    ax.set_ylabel("Return")
    st.pyplot(fig)
