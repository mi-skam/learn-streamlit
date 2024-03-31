import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google.
""")

tickerSymbol = "GOOGL"
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period="1d", start="2014-3-31", end="2024-3-31")

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
