import streamlit as st
from playsound import playsound
from time 
import random

def activate_prank():
 for i in range(3):
  time.sleep(random.randint(120, 300))
  playsound('https://www.soundjay.com/buttons/sounds/beep-02.mp3')


prank_activate_button = st.button('Activate Prank')

if prank_activate_button:
 activate_prank()

