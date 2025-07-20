import streamlit as st
import yfinance as yf
import pandas as pd
from chart import plot_chart

def load_symbols():
    df = pd.read_csv("data/nifty_500.csv")
    return df["Symbol"].tolist()

def fetch_data(symbol, tf):
    tf_map = {"1h": "60m", "2h": "120m", "4h": "240m", "1d": "1d", "1mo": "1mo"}
    df = yf.download(f"{symbol}.NS", period="6mo", interval=tf_map[tf])
    return df

def is_green_candle(df):
    return df["Close"].iloc[-1] > df["Open"].iloc[-1]

def is_support_near(df, line):
    close = df["Close"].iloc[-1]
    ma = df[line].iloc[-1]
    return abs(close - ma) / close < 0.01

def is_monthly_breakout(df):
    return df["High"].iloc[-1] > df["High"].iloc[-2]

def run_scanner(setup, tf):
    for symbol in load_symbols():
        try:
            df = fetch_data(symbol, tf)
            if df.empty:
                continue

            if setup == "200 EMA Support":
                df["EMA200"] = df["Close"].ewm(span=200).mean()
                if is_support_near(df, "EMA200") and is_green_candle(df):
                    st.subheader(symbol)
                    plot_chart(df, symbol, "EMA200")

            elif setup == "30 SMA Support":
                df["SMA30"] = df["Close"].rolling(30).mean()
                if is_support_near(df, "SMA30") and is_green_candle(df):
                    st.subheader(symbol)
                    plot_chart(df, symbol, "SMA30")

            elif setup == "Monthly Breakout" and tf == "1mo":
                if is_monthly_breakout(df):
                    st.subheader(symbol)
                    plot_chart(df, symbol)

        except:
            pass
