import streamlit as st
import time

@st.cache_data
def expensive_computation(x):
    time.sleep(3)  # Simulate a heavy computation
    return x**2

st.write("Square of 4 is:", expensive_computation(4))
