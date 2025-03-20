import streamlit as st
from transformers import pipeline
from PIL import Image
import io
import os

os.environ["TF_USE_LEGACY_KERAS"] = "1"  # Forces TensorFlow to use legacy Keras

def identify_breed(dog_photo):
 dog_breed_detect = pipeline('image-classification', model = 'wesleyacheng/dog-breeds-multiclass-image-classification-with-vit')
 
 dog_breeds_and_scores = []

 for breed in dog_breed_detect(dog_photo):
  dog_breeds_and_scores.append((breed['score'], breed['label']))

 return max(dog_breeds_and_scores)[1].replace('_', ' ')


st.write('<h1>Identify what is your dog breed within few seconds</h1>', unsafe_allow_html = True)

file = st.file_uploader('Your dog photo (may not give good results with multiple dogs)')
button = st.button('Detect Breed')

if button:
 image = Image.open(io.BytesIO(file.getvalue()))

 print(image)
 
 breed = identify_breed(image)

 st.write(breed)

 
