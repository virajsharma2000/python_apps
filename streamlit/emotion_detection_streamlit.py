import streamlit as st
import emotion_in_text_detector as emotion_detector

text = st.text_input('Enter text')
button = st.button('Detect Emotion')

if button:
 emotion = emotion_detector.detect_emotion(text)

 st.write(emotion)
