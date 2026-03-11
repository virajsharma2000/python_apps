import streamlit as st
import streamlit.components.v1 as components
from gtts import gTTS
import os

os.system('sudo apt install espeak')
st.header('Viraj says - YOU ARE JUST A SHIT 💩')

if st.button('Click Me'):
 while True:
  tts = gTTS(text = 'you are just a shit', lang = 'en')
  components.html("""<script type="text/javascript">
            window.open('https://lordofpotty.streamlit.app');
        </script>""")
