import streamlit
import playsound

def play_siren():
 playsound.playsound('https://dl.prokerala.com/downloads/ringtones/files/mp3/nuclear-alarm-14008.mp3')


if streamlit.button('play siren'):
 play_siren()
