import streamlit as st
import plotly.graph_objects as go

def plot_chart(df, symbol, line=None):
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df["Open"], high=df["High"],
        low=df["Low"], close=df["Close"],
        name="Price"))

    if line:
        fig.add_trace(go.Scatter(
            x=df.index, y=df[line], name=line, line=dict(color='blue')))

    fig.update_layout(title=f"{symbol} Chart", xaxis_rangeslider_visible=False)
    st.plotly_chart(fig, use_container_width=True)
