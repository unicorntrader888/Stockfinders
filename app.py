import streamlit as st
from scanner import run_scanner

st.set_page_config(page_title="StockFinders", layout="wide")
st.title("📈 StockFinders - Nifty 500 Scanner")

setup_option = st.selectbox("Select Setup", ["200 EMA Support", "30 SMA Support", "Monthly Breakout"])
timeframe = st.selectbox("Select Timeframe", ["1h", "2h", "4h", "1d", "1mo"])

if st.button("🚀 Start Scan"):
    run_scanner(setup_option, timeframe)
