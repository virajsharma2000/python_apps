import streamlit as st
import sounddevice as sd
import numpy as np

def detect_loud_volume(indata, frames, time, status):
 volume_norm = np.linalg.norm(indata) * 10

 if volume_norm >= 0.15:
  st.write('<script>alert("YOU ALL ARE TOO NOISY!! SHUP UP!! NOW VOICE OVER!!")</script>', unsafe_allow_html = True)

def moniter_loud_noise():
 with sd.InputStream(callback = detect_loud_volume, channels = 1, samplerate = samplerate):
  pass


activate_button = st.button('Activate Noise Moniter')

if activate_button:
 moniter_loud_noise()
