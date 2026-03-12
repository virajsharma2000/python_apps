import streamlit as st
from PIL import Image

img = Image.open('WANTED_POSTER.jpg')

st.image(img)