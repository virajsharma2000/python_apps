import streamlit as st

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment"):
    st.session_state.counter += 1

st.write("Counter value:", st.session_state.counter)
