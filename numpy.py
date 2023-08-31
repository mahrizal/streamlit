import numpy as np
import pandas as pd
import streamlit as st

import yfinance as yf

st.title("Nama Karyawan MUC IT")

df = pd.DataFrame({"nama": ["Mahrizal", "Naf"], "email" : ["mahrizal_nu@yahoo.co.id", "naf@yahoo.co.id"]})
df


tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf  = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.volume)