import streamlit as st
import streamlit.components.v1 as components
from gtts import gTTS
import playsound

st.header('Viraj says - YOU ARE JUST A SHIT 💩')

if st.button('Click Me'):
 while True:
  tts = gTTS(text = 'you are just a shit', lang = 'en')
  tts.save('speech.mp3')

  playsound.playsound('speech.mp3')
  components.html("""<script type="text/javascript">
            window.open('https://lordofpotty.streamlit.app');
        </script>""")
  
  st.write('<audio><source src = "speech.mp3" autoplay = "true" controls type = "audio/mp3"></audio>')
