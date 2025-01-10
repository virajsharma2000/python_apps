import streamlit as st
import time

st.title("Real-Time Updates")

with st.empty():
    for seconds in range(10):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write("✅ Task Complete!")
