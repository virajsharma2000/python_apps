import streamlit as st

def check_overweight_or_underweight(age, weight):
 if age >= 1 and age <= 10:
  appropriate_weight = 2 * age + 8

  return 'over weight' if weight > appropriate_weight else 'under weight' if weight < appropriate_weight else 'perfect weight'

 elif age >= 11 and age <= 18:
  appropriate_weight = 3 * age

  return 'over weight' if weight > appropriate_weight else 'under weight' if weight < appropriate_weight else 'perfect weight'

 else:
  st.error('age must be between 1 and 18')


st.write('<h1>Check whether your child is having underweight, overweight or perfect weight within seconds!!</h1>', unsafe_allow_html = True)

age = st.text_input('Enter your child\'s age')
weight = st.text_input('Enter your child\'s weight')

if st.button('Check'):
 overweight_or_underweight = check_overweight_or_underweight(int(age), float(weight))
 
 if overweight_or_underweight is not None:
  st.success(f'your child is {overweight_or_underweight}')

 