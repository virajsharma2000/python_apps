import streamlit as st
import diwali_snack_recipies

snacks = diwali_snack_recipies.get_snack_options()

st.write('choose any snack and start making your snack')

for snack in snacks:
 if st.button(snack):
  recipie = diwali_snack_recipies.get_snack_recipies(snack)

  st.write('ingredients - ')

  for ingredient in recipie[0]:
   st.write(ingredient)

  st.write(' ')
  
  st.write('instructions - ')

  for instruction in recipie[1]:
   st.write(instruction)
