import streamlit as st

def parse_samosa(samosa_code):
 samosa_code = samosa_code.replace(' ', '')
 
 samosa_json_data = []
 
 for samosa in samosa_code.split('+'):
  samosa = samosa.split('x')

  if samosa[0].split(']')[0].split('[')[0] == 'samosa':
   samosa_type = samosa[0].split(']')[0].split('[')[1]
   samosa_quantity = int(samosa[1])

   samosa_json_data.append({'samosa_type':samosa_type, 'samosa_quantity':samosa_quantity})

 return samosa_json_data


st.title('A online kiddish samosa commandlines parser')

st.header('syntax - samosa[samosa_type] x samosa_quantity + samosa[samosa_type] x samosa_quantity')

samosa_code = st.text_area('Type your samosa code here', height = 500)
samosa_parse_button = st.button('parse samosa code')

if samosa_parse_button:
 json_output = parse_samosa(samosa_code)

 st.json(json_output)

