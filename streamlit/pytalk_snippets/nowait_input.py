import streamlit as st

name = st.text_input('Enter your name:')
#if name: - UNCOMMENT the check
st.write(f'Hello, {name}!')
