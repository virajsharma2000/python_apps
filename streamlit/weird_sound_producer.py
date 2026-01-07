import streamlit as st
import numpy as np

st.title('MAKE WEIRD NOISES AND SCARE PEOPLE AND CAUSE PANICS EASIALLY!!! 😈')

def make_weird_noises(duration):
 fs = 44100

 sound = np.array([[0.9] * 100 + [-0.9] * 100] * ((fs * duration) // 2 // 100)).flatten()

 st.audio(sound, sample_rate = fs)

duration = st.text_input('Enter duration here:')

if st.button('Play Sound'):
 make_weird_noises(int(duration))