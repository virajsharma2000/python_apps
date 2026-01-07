import streamlit as st
import sounddevice as sd
import numpy as np

st.title('MAKE WEIRD NOISES AND SCARE PEOPLE AND CAUSE PANICS EASIALLY!!! 😈')

def make_weird_noises(duration):
 fs = 44100

 sound = np.array([[0.9] * 1000 + [-0.9] * 1000] * ((fs * duration) // 2 // 1000)).flatten()

 sd.play(sound, samplerate = fs)
 sd.wait()


duration = st.text_input('Enter duration here:')

if st.button('Play Sound'):
 make_weird_noises(int(duration))