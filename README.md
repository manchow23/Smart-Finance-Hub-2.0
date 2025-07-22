# 📊 Smart Finance Hub 2.0

Welcome to **Smart Finance Hub 2.0** — an all-in-one, interactive finance dashboard that helps you **analyze**, **predict**, and **plan** your investments, all in a slick Streamlit app.

> 🔁 Updated & upgraded from my earlier project version with more features, better UI, and real-time interaction!

---

## 🚀 What's New in 2.0?

✅ Now a **fully interactive Streamlit web app**  
✅ Support for **Dark/Light mode toggle**  
✅ Better **UI styling** with custom fonts, metrics, and themes  
✅ Added **daily returns summary** and **performance metrics**  
✅ Expanded and modularized for better maintainability

---

## 🧩 Features & Modules

### 1. 📉 Market Crash Analyzer
Analyze historic market crashes and big red days with:
- Daily returns calculation
- Visual crash markers for significant drops (like 2008, 2020)
- Dynamic threshold setting to define "crash"

### 2. 🪙 Mutual Fund SIP Planner
Visual tool for SIP investment planning:
- Select fund types (Large Cap, Mid Cap, Small Cap)
- Set SIP amount, duration, and expected return
- Bar charts of yearly investment growth
- Total investment vs expected corpus

### 3. 📈 Portfolio Optimizer
Smart asset allocation powered by simulation:
- Random portfolios with return & volatility stats
- Sharpe ratio calculation to find optimal risk-adjusted mix
- Heatmaps of asset weights
- Scatter plot of return vs volatility

### 4. 📊 Quantitative Analysis Module
Statistical deep-dive into market behavior:
- Daily return histograms (with KDE)
- Rolling 30-day volatility plot
- Predictive modeling (linear regression on selected stocks)

### 5. 🔍 Daily Returns Summary (New!)
Quick overview of:
- Recent daily returns (tabular view)
- Average return per stock/ticker
- Helps identify best/worst performers

---

## ⚙️ Tech Stack

- **Python**
- **Streamlit**
- **Pandas, NumPy, yFinance**
- **Matplotlib, Seaborn**
- **Scikit-learn** (for modeling in notebook version)

---

## 🛠️ Setup Instructions

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/smart-finance-hub.git
   cd smart-finance-hub

2. **Installment Requirements:**
    ```bash
    pip install -r requirements.txt

3. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
