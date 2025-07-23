# Smart Finance Hub 2.0 

Welcome to **Smart Finance Hub 2.0** — an all-in-one, interactive finance dashboard that helps you **analyze**, **predict**, and **plan** your investments, all in a slick Streamlit app.

> 🔁 Updated & upgraded from my earlier project version with more features, better UI, and real-time interaction!

It transforms raw market data into insights that help you:

✅**Understand market crashes**

✅**Plan SIP investments**

✅**Build optimized portfolios**

✅**Perform quantitative analysis**

Originally started as a basic stock analysis tool, it evolved into a feature-rich financial hub.

---

 ## ✨ Features
### 1. Market Crash Analyzer ###
Detects daily market crashes beyond a threshold (e.g., -5%).

Highlights major events like the 2008 & 2020 crashes.

Plots daily returns and crash points using intuitive charts.

<img width="1918" height="821" alt="image" src="https://github.com/user-attachments/assets/4281d3fc-42c9-437d-aa7e-74db08ce6cee" />


### 2. Mutual Fund Planner ###
Calculate SIP (Systematic Investment Plan) growth.

Input: monthly investment, duration, expected annual return.

Displays future wealth projection with charts & key metrics.

<img width="1919" height="816" alt="image" src="https://github.com/user-attachments/assets/118a013a-0687-44fc-9888-3f8be5817948" />


### 3. Portfolio Optimization ###
Build your own multi-stock portfolio.

Simulates thousands of portfolios to find max Sharpe Ratio (best return vs risk).

Outputs optimal allocation + risk-return visualization.

<img width="1919" height="826" alt="image" src="https://github.com/user-attachments/assets/16520d2b-722c-4413-a76e-5d222327d5f6" />


### 4. Quantitative Finance Analytics ###
View daily return distributions.

Measure rolling volatility (30-day) to gauge risk.

Predict price trends using Linear Regression & visualize them.

<img width="1919" height="822" alt="image" src="https://github.com/user-attachments/assets/bb1f5f9a-438f-4d82-80e2-86858e4e09e0" />

---

## 🛠 Tech Stack
Python – Core Programming

Streamlit – Interactive Dashboard

yFinance – Stock Data API

Pandas & NumPy – Data Processing

Matplotlib & Seaborn – Data Visualization

Scikit-learn – Machine Learning (Linear Regression)

---

## 📂 Project Structure
bash
Copy
Edit
Smart-Finance-Hub/
│
├── app2_0.py              # Streamlit App
├── Helper                  
      ├── crash_analysis.py   #Crash detection logic
      ├── mutual_fund.py      #Fund planner logic
      ├── optimizer.py        #Portfolio logic
      ├── quant_stats.py      #Quantitative methods
├── requirements.txt       # Dependencies
├── data/                  # (Optional) Static CSV Inputs
└── README.md              # Documentation

---

## 🚀 Getting Started
Clone the repo and run:

bash
Copy
Edit
git clone https://github.com/manchow23/Smart-Finance-Hub-2.0
cd smart-finance-hub
pip install -r requirements.txt
streamlit run app2_0.py

---

## 📈 What You’ll Learn
- How to use real-time stock market data from APIs

- How to optimize investment portfolios mathematically

- Basics of quantitative finance modeling (returns, risk, Sharpe ratio)

- Building interactive data apps with Streamlit

---

## Future Roadmap
 Real-time crash alerts

 Advanced portfolio strategies

 Cloud deployment for live public use



