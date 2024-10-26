import streamlit as st
import diwali_wish_generator

phone_number_or_group_id = st.text_input('Enter phone number')
button = st.button('Generate and Send Diwali Wish')

if button:
   diwali_wish = diwali_wish_generator.generate_diwali_wish()

   st.write(diwali_wish)

   diwali_wish_in_url_text = ''

   for charecter in diwali_wish:
    if charecter == ' ':
     diwali_wish_in_url_text += '%20'

    elif charecter == '\n':
     diwali_wish_in_url_text += '%0A'

    else:
     diwali_wish_in_url_text += charecter
    
   st.write('<a href = "https://web.whatsapp.com/send?phone={}&text={}">Send Diwali Wish</a>'.format(phone_number_or_group_id, diwali_wish_in_url_text), unsafe_allow_html = True)
