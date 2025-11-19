import streamlit as st
import random
from fpdf import FPDF
import json

def generate_json_id(name, age, grade, section, blood_group, mother_name, father_name):
 parents = [{'parent_name':mother_name, 'parent_type':'mother'}, {'parent_name':father_name, 'parent_type':'father'}]

 random.shuffle(parents)

 json_text = json.dumps({"name":name, "age":age, "grade":grade, "section":section, "blood_group":blood_group, "parents":parents}, indent = 4)

 pdf = FPDF()

 pdf.add_page()
 pdf.set_font('Arial')

 for line in json_text.splitlines():
  pdf.cell(100, 5, txt = line, ln = True, align = 'L')

 pdf.output('weird_techy_icard.pdf')

 with open('weird_techy_icard.pdf', 'rb') as f:
  st.download_button('download your icard', f, file_name = 'alien_id.pdf')


name = st.text_input('Enter name: ')
age = st.text_input('Enter age: ')
grade = st.text_input('Enter grade: ')
section = st.text_input('Enter section: ')
blood_group = st.text_input('Enter blood group: ')
mother_name = st.text_input('Enter your mother name: ')
father_name = st.text_input('Enter your father name: ')

if st.button('Generate your id!'):
 generate_json_id(name, int(age), int(grade), section, blood_group, mother_name, father_name)