import streamlit as st
import emotion_in_text_detector as emotion_detector

st.write('<h1>this tool detects emotion in text with my simple made module called emotion_in_text_detector</h1>')

text = st.text_input('Enter text')
button = st.button('Detect Emotion')

if button:
 emotion = emotion_detector.detect_emotion(text)

 st.write(emotion)
