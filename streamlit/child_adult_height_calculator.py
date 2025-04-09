import streamlit as st

height_percent_by_age = {
    1: 50,     
    2: 60,    
    3: 65,
    4: 70,
    5: 75,
    6: 77,
    7: 80,
    8: 82,
    9: 85,
    10: 88,
    11: 91,
    12: 94,
    13: 96,
    14: 98,
    15: 99,
    16: 99.5,
    17: 99.8,
}
 

def calculate_adult_height(age, current_height):
 if age >= 1 and age <= 17:
  return round(current_height / height_percent_by_age.get(age) * 100)
 
 else:
  st.error('Age must be between 1 and 17')


st.write('<h1>Calculate your adolescent  or your child\'s adult hood height within seconds!!</h1>', unsafe_allow_html=True)    

height = st.text_input('your child\'s height')
age = st.text_input('your child\'s age')

if st.button('Calculate'):
 height = calculate_adult_height(int(age), float(height))
 
 if height is not None:
  st.success(f'height your child\'s adult height will be - {height} cm')