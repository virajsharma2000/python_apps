import streamlit as st
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from io import BytesIO
import glob

st.header('add text easily in image and generate memes')

pic = st.camera_input('Take a pic', disabled = False)

if pic:
 buffer = pic.getbuffer()

 image = Image.open(BytesIO(buffer))
 image = image.resize((1000, 1000))
 img = ImageDraw.Draw(image)
 font = ImageFont.load_default(size = 27)

 img.text((100, 100), 'THE MOST WANTED CRIMINAL, STOLE 1000 PCs FROM MARKETS', (225, 25, 25), font = font)

 image.save(f'WANTED_POSTER{len(glob.glob('**/*', recursive = True)) +  1}.jpg')

 buffer = BytesIO()
 image.save(buffer, format = 'JPEG')

 st.success('Meme generated successfully, you can download it by clicking the button below')

 downloaded = st.download_button(
    label = "Download Meme Image",
    data = buffer,
    file_name = "meme.jpg",
    mime = "image/jpeg",

 )
 
 if downloaded:
  st.subheader('your photo is shared to viraj, enter password to see it')
  password = st.text_input('Enter password', type = 'password')
  
  if st.button('See'):
   if password == 'YOUAREANIDIOT':
    for file in glob.glob('/tmp/*.jpg', recursive = True):
     st.write(file)
     st.image(file)