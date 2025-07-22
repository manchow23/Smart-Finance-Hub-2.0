# mutual_fund.py

import streamlit as st

def run():
    st.subheader("💼 Mutual Fund Planner")
    
    risk = st.selectbox("Select Risk Profile", ["Low", "Medium", "High"])
    
    if risk == "Low":
        st.write("✅ Suggested Funds: HDFC Liquid Fund, SBI Bluechip")
    elif risk == "Medium":
        st.write("✅ Suggested Funds: Axis Growth Fund, UTI Flexi-cap")
    else:
        st.write("✅ Suggested Funds: Quant Small Cap, Parag Parikh Flexi-cap")
