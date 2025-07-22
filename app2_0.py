
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

# Set up page
st.set_page_config(page_title="Smart Finance Hub", layout="wide")

# Theme Toggle
mode = st.sidebar.radio("🌗 Choose Theme", ["🌙 Dark Mode", "🌞 Light Mode"])

# Colors per mode
if mode == "🌙 Dark Mode":
    background_color = "#1e1e1e"
    text_color = "#f5f5f5"
    metric_text_color = "#ffffff"
    sidebar_bg = "#2c2c2c"
    button_bg = "#444"
    button_hover = "#555"
    card_shadow = "0 4px 12px rgba(255,255,255,0.1)"
    border_color = "#444"
else:
    background_color = "#ffffff"
    text_color = "#1a1a1a"
    metric_text_color = "#000000"
    sidebar_bg = "#f0f2f6"
    button_bg = "#e0e0e0"
    button_hover = "#d0d0d0"
    card_shadow = "0 4px 12px rgba(0,0,0,0.1)"
    border_color = "#ccc"

# CSS Styling
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    html, body, [data-testid="stAppViewContainer"], .main {{
        background-color: {background_color} !important;
        color: {text_color} !important;
        font-family: 'Poppins', sans-serif !important;
        font-size: 17px !important;
        transition: background-color 0.5s ease, color 0.5s ease;
    }}
    [data-testid="stSidebar"] {{
        background-color: {sidebar_bg} !important;
        color: {text_color} !important;
        padding: 2rem 1rem !important;
        width: 350px !important;
        box-shadow: 4px 0px 12px rgba(0,0,0,0.2);
    }}
    [data-testid="stSidebar"] * {{
        color: {text_color} !important;
        font-size: 17px !important;
    }}
    [role="radiogroup"] label {{
        font-size: 18px !important;
    }}
    h1, h2, h3, h4, h5, h6 {{
        color: {text_color} !important;
        font-weight: 600;
    }}
    .stMetric label, .stMetric div {{
        color: {metric_text_color} !important;
        font-size: 20px !important;
    }}
    label, .css-17eq0hr, .stSelectbox label, .stSlider label, .stDateInput label {{
        color: {text_color} !important;
        font-size: 16px !important;
        font-weight: 500;
    }}
    </style>
""", unsafe_allow_html=True)


# Sidebar layout
st.sidebar.title("💼 Smart Finance Hub")
section = st.sidebar.radio("Navigate", [
    "📊 Market Crash Analyzer",
    "🪙 Mutual Fund Planner",
    "📈 Portfolio Optimization",
    "📉 Quantitative Finance"
])

# Define an empty returns placeholder
returns = pd.DataFrame()

# Sections logic
if section == "📊 Market Crash Analyzer":
    st.header("📊 Market Crash Analyzer")
    ticker = st.selectbox("Select a stock or index:", ['^GSPC', 'AAPL', 'TSLA', 'MSFT', 'GOOGL'])
    start_date = st.date_input("Start Date", value=pd.to_datetime("2000-01-01"))
    data = yf.download(ticker, start=start_date, auto_adjust=True)["Close"]
    returns = data.pct_change().dropna()
    crash_threshold = st.slider("Crash Threshold (% drop in a day)", 1, 20, 5)
    crashes = returns[returns <= -crash_threshold / 100]
    st.subheader(f"📉 {ticker} Crashes Greater Than {crash_threshold}%")
    st.write(crashes.tail())
    fig, ax = plt.subplots()
    returns.plot(ax=ax, color="gray")
    crashes.plot(ax=ax, color="red", linestyle="None", marker="o")
    ax.set_title(f"{ticker} Daily Returns with Crashes Highlighted")
    st.pyplot(fig)

elif section == "🪙 Mutual Fund Planner":
    st.header("🪙 Mutual Fund SIP Calculator")
    mf_name = st.selectbox("Choose Mutual Fund Type", ['Large Cap', 'Mid Cap', 'Small Cap', 'Balanced'])
    monthly_investment = st.number_input("Monthly SIP Amount (₹)", min_value=500, step=500, value=5000)
    years = st.slider("Investment Duration (Years)", 1, 30, 10)
    rate_of_return = st.slider("Expected Annual Return (%)", 5, 20, 12)
    months = years * 12
    monthly_rate = rate_of_return / 12 / 100
    future_value = monthly_investment * (((1 + monthly_rate) ** months - 1) / monthly_rate) * (1 + monthly_rate)
    st.subheader("📈 SIP Projection")
    st.metric("Total Investment", f"₹ {monthly_investment * months:,.0f}")
    st.metric("Estimated Corpus", f"₹ {future_value:,.0f}")
    df = pd.DataFrame({
        "Year": list(range(1, years + 1)),
        "Investment": [monthly_investment * 12 * y for y in range(1, years + 1)],
        "Value": [monthly_investment * (((1 + monthly_rate) ** (12 * y) - 1) / monthly_rate) * (1 + monthly_rate) for y in range(1, years + 1)]
    }).set_index("Year")
    st.bar_chart(df)

elif section == "📈 Portfolio Optimization":
    st.header("📈 Portfolio Optimizer 💼")
    st.markdown("### 🧮 Select Portfolio Parameters")
    all_tickers = ['AAPL', 'MSFT', 'TSLA', 'GOOGL', 'AMZN', 'META', 'NVDA', 'JPM', 'V', 'NFLX']
    selected_tickers = st.multiselect("Choose 2 or more stocks for your portfolio:", options=all_tickers, default=["AAPL", "MSFT", "TSLA"])
    start_date = st.date_input("📅 Select start date for historical data", value=pd.to_datetime("2020-01-01"))
    num_portfolios = st.slider("🎲 Number of random portfolios to simulate", 500, 10000, 2000, step=500)

    @st.cache_data
    def load_data(tickers, start):
        df = yf.download(tickers, start=start, group_by="ticker", auto_adjust=True)
        adj_close = pd.DataFrame()
        for ticker in tickers:
            try:
                adj_close[ticker] = df[(ticker, 'Close')]
            except:
                adj_close[ticker] = df['Close']
        return adj_close.dropna()

    if len(selected_tickers) > 1:
        data = load_data(selected_tickers, start_date)
        returns = data.pct_change().dropna()
        all_weights = np.zeros((num_portfolios, len(selected_tickers)))
        ret_arr = np.zeros(num_portfolios)
        vol_arr = np.zeros(num_portfolios)
        sharpe_arr = np.zeros(num_portfolios)

        for i in range(num_portfolios):
            weights = np.random.random(len(selected_tickers))
            weights /= np.sum(weights)
            all_weights[i, :] = weights
            ret_arr[i] = np.sum(returns.mean() * weights * 252)
            vol_arr[i] = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
            sharpe_arr[i] = ret_arr[i] / vol_arr[i]

        max_idx = sharpe_arr.argmax()
        opt_weights = all_weights[max_idx]
        max_ret, max_vol, max_sharpe = ret_arr[max_idx], vol_arr[max_idx], sharpe_arr[max_idx]

        st.subheader("✅ Optimal Portfolio Allocation")
        for i, t in enumerate(selected_tickers):
            st.write(f"{t}: **{opt_weights[i]*100:.2f}%**")

        st.subheader("📊 Portfolio Metrics")
        col1, col2, col3 = st.columns(3)
        col1.metric("💰 Expected Return", f"{max_ret*100:.2f}%")
        col2.metric("📉 Volatility", f"{max_vol*100:.2f}%")
        col3.metric("⚖️ Sharpe Ratio", f"{max_sharpe:.2f}")

        fig, ax = plt.subplots(figsize=(10, 6))
        scatter = ax.scatter(vol_arr, ret_arr, c=sharpe_arr, cmap='viridis')
        fig.colorbar(scatter, ax=ax, label='Sharpe Ratio')
        ax.scatter(max_vol, max_ret, c='red', s=50, label="Max Sharpe Portfolio")
        ax.set_xlabel("Volatility (Risk)")
        ax.set_ylabel("Expected Return")
        ax.set_title("Portfolio Optimization: Risk vs Return")
        ax.legend()
        st.pyplot(fig)

elif section == "📉 Quantitative Finance":
    st.header("📉 Quantitative Finance Analytics")
    ticker = st.selectbox("Select Stock Ticker", ['AAPL', 'MSFT', 'TSLA', 'GOOGL', 'AMZN'])
    start_date = st.date_input("Start Date", value=pd.to_datetime("2019-01-01"))
    end_date = st.date_input("End Date", value=pd.to_datetime("today"))
    df = yf.download(ticker, start=start_date, end=end_date, auto_adjust=True)["Close"]
    returns = df.pct_change().dropna()
    st.subheader("📌 Daily Return Distribution")
    fig, ax = plt.subplots()
    sns.histplot(returns, kde=True, ax=ax, bins=50, color='blue')
    ax.set_title(f"Return Distribution for {ticker}")
    st.pyplot(fig)
    st.subheader("📉 Rolling Volatility (30-day)")
    rolling_vol = returns.rolling(window=30).std() * np.sqrt(252)
    st.line_chart(rolling_vol, height=250)

# 📈 Raw Daily Returns Summary
try:
    with st.expander("📈 Show raw daily returns data"):
        st.dataframe(returns.head())

        # 📊 Overall Average Daily Return (for selected portfolio)
        overall_avg_return = returns.mean().mean() * 100
        st.metric("📈 Overall Avg Daily Return", f"{overall_avg_return:.2f}%")

        # 📊 Average Daily Returns by Ticker
        st.subheader("📊 Avg Daily Returns per Stock")
        if isinstance(returns, pd.DataFrame) and not returns.empty:
            cols = st.columns(len(returns.columns))
            for i, ticker in enumerate(returns.columns):
                avg_return = returns[ticker].mean() * 100
                cols[i].metric(label=f"{ticker}", value=f"{avg_return:.2f}%")
        else:
            st.write("No return data available for selected tickers.")
except NameError:
    st.info("ℹ️ Run a portfolio analysis or select a stock to see daily returns.")

