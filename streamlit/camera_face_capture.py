import streamlit as st
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from io import BytesIO

st.header('add text easily in image and generate memes')

pic = st.camera_input('Take a pic', disabled = False)

if pic:
 buffer = pic.getbuffer()

 image = Image.open(BytesIO(buffer))
 image = image.resize((1000, 1000))
 img = ImageDraw.Draw(image)
 font = ImageFont.load_default(size = 27)

 img.text((100, 100), 'THE MOST WANTED CRIMINAL, STOLE 1000 PCs FROM MARKETS', (225, 0, 0), font = font)
 image.save('WANTED_POSTER.jpg')

 buffer = BytesIO()
 image.save(buffer, format = 'JPEG')

 st.success('Meme generated successfully, you can download it by clicking the button below')

 st.download_button(
    label = "Download Meme Image",
    data = buffer,
    file_name = "meme.jpg",
    mime = "image/jpeg",

 )
 
 st.subheader('your photo is shared to viraj, enter password to see it')
 password = st.text_input('Enter password', type = 'password')

 if password == 'YOUAREANIDIOT':
  st.image('WANTED_POSTER.jpg')