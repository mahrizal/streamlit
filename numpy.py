import numpy as np
import pandas as pd
import streamlit as st

import yfinance as yf

st.title("Nama Karyawan MUC IT")

df = pd.DataFrame({"nama": ["Mahrizal", "Naf"], "email" : ["mahrizal_nu@yahoo.co.id", "naf@yahoo.co.id"]})
df
