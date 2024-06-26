import streamlit as st
import requests

def get_joke():
 response = requests.get('https://v2.jokeapi.dev/joke/Programming')

 json = response.json()
 
 joke_type = json['type']

 if joke_type == 'single':
  joke = json['joke']

 if joke_type == 'twopart':
  joke = json['setup'] + '\n' + json['delivery']

 return joke


if st.button('Get Joke'):
 joke = get_joke()

 st.write(joke)



