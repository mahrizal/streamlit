import numpy as np
import pandas as pd
import streamlit as st

st.title("Nama Karyawan MUC IT")

df = pd.DataFrame({"nama": ["Mahrizal", "Naf"], "email" : ["mahrizal_nu@yahoo.co.id", "naf@yahoo.co.id"]})
df

import matplotlib.pyplot as plt

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # 👈 Draw a Matplotlib chart
