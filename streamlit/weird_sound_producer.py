import streamlit as st
import numpy as np

st.title('MAKE WEIRD NOISES AND SCARE PEOPLE AND CAUSE PANICS EASIALLY!!! 😈')

def make_weird_noises(duration):
 fs = 44100

 sound = np.array([[0.9] * 500 + [-0.9] * 500] * ((fs * duration) // 2 // 500)).flatten()

 st.audio(sound, sample_rate = fs)

duration = st.text_input('Enter duration here:')

if st.button('Play Sound'):
 make_weird_noises(int(duration))