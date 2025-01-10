import streamlit as st
import requests

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
data = response.json()

st.write("Bitcoin Price:", data["bpi"]["USD"]["rate"])
