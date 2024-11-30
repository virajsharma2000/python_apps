import streamlit as st
import sounddevice as sd
import numpy as np

def detect_loud_volume(indata, frames, time, status):
 volume_norm = np.linalg.norm(indata) * 10

 if volume_norm >= 0.15:
  st.write('<h1>YOU ALL ARE TOO NOISY!! SHUP UP!! NOW VOICE OVER!!</h1>', unsafe_allow_html = True)

def moniter_loud_noise():
 with sd.InputStream(callback = detect_loud_volume, channels = 1):
  sd.sleep(21600000)

activate_button = st.button('Activate Noise Moniter')

if activate_button:
 moniter_loud_noise()
