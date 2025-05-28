import streamlit as st
import json

def format_json(string_json):
 return json.dumps(json.loads(string_json), indent = 4)


left_col, right_col = st.columns([2, 1])

with left_col:
 json_data = st.text_area('Enter your json', height = 500)

formatted_json = ""

if st.button('format json'):
 formatted_json = format_json(json_data)

with right_col:
 st.text_area('formatted json', value = formatted_json, height = 500)

