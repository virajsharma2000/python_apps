import streamlit
import random

def generate_random_letters():
 letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

 random_letters = ''
 
 for i in range(5):
  random_letters += random.choice(letters)

 return random_letters


streamlit.write('<p style = "font-size:18px;">1.{}</p>'.format(generate_random_letters()),unsafe_allow_html = True)
streamlit.write('<p style = "font-size:16px;">2.{}</p>'.format(generate_random_letters()),unsafe_allow_html = True)
streamlit.write('<p style = "font-size:14px;">3.{}</p>'.format(generate_random_letters()),unsafe_allow_html = True)
streamlit.write('<p style = "font-size:12px;">4.{}</p>'.format(generate_random_letters()),unsafe_allow_html = True)
streamlit.write('<p style = "font-size:10px;">5.{}</p>'.format(generate_random_letters()),unsafe_allow_html = True)

last_line_number_able_to_see = streamlit.text_input("which last line number you are able to see")

if streamlit.button('get font size'):
 if not int(last_line_number_able_to_see) > 6:
  font_size = 18 - (int(last_line_number_able_to_see) - 1) * 2

  streamlit.write(font_size)

 else:
  streamlit.write('exceeding maximum line number')
