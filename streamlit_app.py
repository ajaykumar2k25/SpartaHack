import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(1, 2) / [10, 10] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)

df = pd.DataFrame(
    np.random.randn(1, 2) / [50, 50] + [35.76, -12.4],
    columns=['lat', 'lon'])

st.map(df)
