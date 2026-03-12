import streamlit as st
from PIL import Image

img = Image.open('wanted_poster.jpg')

st.image(img)