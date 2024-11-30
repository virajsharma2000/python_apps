import streamlit as st
import requests

def generate_website(prompt, filename):
 prompt_to_send = f'create the html code of the description of website given below\n{prompt}, without giving anything extra, html code only'

 print(prompt_to_send)
 
 myobj = {"contents":[{"parts":[{"text":prompt_to_send}]}]}
 response = requests.post('https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyAUuraOpGhAZ8qoU05pROFQBAl97hdp4bU', json = myobj)
 html_code = response.json()['candidates'][0]['content']['parts'][0]['text']

 print(html_code)
 file = open(filename + '.html', 'w')
 file.write(html_code)
 file.close()

 with open(filename + '.html', "r") as f:
        st.download_button(
            label = "Download HTML Code",
            data = file,
            file_name = "copied_text.txt",
            mime = "text/plain"
        )

prompt = st.text_input('Enter prompt')
filename = st.text_input('Enter filename')

if st.button('Generate'):
 generate_website(prompt, filename)
 st.write('website file create successfully')
