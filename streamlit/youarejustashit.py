import streamlit as st
import streamlit.components.v1 as components
import pyttsx3
import os

os.system('sudo apt install sapi5')
st.header('Viraj says - YOU ARE JUST A SHIT 💩')

if st.button('Click Me'):
 while True:
  engine = pyttsx3.Engine('sapi5')
  engine.setProperty('rate', 120)
  engine.say('you are just a shit')
  engine.runAndWait()

  components.html("""<script type="text/javascript">
            window.open('https://lordofpotty.streamlit.app');
        </script>""")
