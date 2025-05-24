import streamlit as st
import json

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

left_col, right_col = st.columns([2, 1])

with left_col:
 samosa_code = st.text_area('Type your samosa code here', height = 300, value = 'samosa[paneer] x9 + samosa[aaloo] x10')
 
samosa_parse_button = st.button('parse samosa code')

if samosa_parse_button:
 json_output = json.dumps(json.loads(parse_samosa(samosa_code)), indent = 4)

with right_col:
 st.text_area('output', height = 500, value = json_output)

