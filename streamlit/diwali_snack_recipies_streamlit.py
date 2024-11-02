import streamlit as st
import diwali_snack_recipies

for snack in diwali_snack_recipies.get_snack_options():
 st.write(snack)

st.write(' ')

snack_name = st.text_input('Enter snack name from above menu')
healthy_or_tasty = st.text_input('snack should be healthy/tasty')

if st.button('Get Recipie'):
 recipie = diwali_snack_recipies.get_snack_recipies(snack_name, healthy = healthy_or_tasty == 'healthy', tasty = healthy_or_tasty == 'tasty')

 st.write('ingredients - ')

 for ingredient in recipie[0]:
  st.write(ingredient)

 st.write(' ')

 st.write('instructions - ')

 for instruction in recipie[1]:
  st.write(instruction)

