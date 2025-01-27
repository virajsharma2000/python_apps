import streamlit as st
import requests
import os
import dotenv

st.title('CSR Application')

st.subheader('Details of organisation')
type_of_organisation = st.selectbox('Type of organisation', ('Education institution', 'Private company', 'Trust', 'NGO', 'Foundation', 'Govt. institution'))
name_of_organisation = st.text_input('Enter the organisation name')

st.subheader('Activity Details')
number_of_people_to_involve = st.slider("Number of people as volenteers", 100, 1000)
budget_of_csr = st.slider('Budget of CSR', 100000, 1000000000)
activity_type = st.selectbox('Type of activity', ('Feeding Drive', 'Cleaning Drive', 'Create shelters for animals'))

if st.button('Generate Plan'):
 dotenv.load_dotenv()
 api_key = os.environ.get('API_KEY')
 
 prompt = f"I am from {type_of_organisation} and this organisation is {type_of_organisation} and I want to do {activity_type} I have {number_of_people_to_involve} volunteers to do this activity and I have Rs.{budget_of_csr} to do my activity according to this information tell me the plan and the location which other organisations have not done and is very unique"

 myobj = {"contents":[{"parts":[{"text":prompt}]}]}
 
 response = requests.post(f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}", json = myobj)
 plan = response.json()['candidates'][0]['content']['parts'][0]['text']

 st.write(plan)
