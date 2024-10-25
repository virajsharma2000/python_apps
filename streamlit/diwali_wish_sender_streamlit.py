import streamlit as st
import diwali_wish_sender

st.write('<h1>my streamlit app to send diwali wish by enterting a phone number of group name, it uses a simple module created by me called diwali_wish_sender</h1>', unsafe_allow_html = True)

phone_number_or_gruop_id = st.text_input('Enter phone number or group id')
button = st.button('Send Diwali Wish')

if button:
 diwali_wish_sender.send_diwali_wish(phone_number_or_gruop_id)

