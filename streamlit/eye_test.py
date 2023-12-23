import streamlit
import random

def generate_random_letters():
 letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

 random_letters = ''
 
 for i in range(5):
  random_letters += random.choice(letters)

 return random_letters

streamlit.write('stand 20 feet away from this chart \n\n')

streamlit.write('<p style = "font-size:152px;">1.{}</p>'.format(generate_random_letters()),unsafe_allow_html = True)
streamlit.write('<p style = "font-size:130px;">2.{}</p>'.format(generate_random_letters()),unsafe_allow_html = True)
streamlit.write('<p style = "font-size:108px;">3.{}</p>'.format(generate_random_letters()),unsafe_allow_html = True)
streamlit.write('<p style = "font-size:87px;">4.{}</p>'.format(generate_random_letters()),unsafe_allow_html = True)
streamlit.write('<p style = "font-size:65px;">6.{}</p>'.format(generate_random_letters()),unsafe_allow_html = True)
streamlit.write('<p style = "font-size:48px;">7.{}</p>'.format(generate_random_letters()),unsafe_allow_html = True)
streamlit.write('<p style = "font-size:33px;">8.{}</p>'.format(generate_random_letters()),unsafe_allow_html = True)
streamlit.write('<p style = "font-size:21px;">9.{}</p>'.format(generate_random_letters()),unsafe_allow_html = True)
streamlit.write('<p style = "font-size:15px;">10.{}</p>'.format(generate_random_letters()),unsafe_allow_html = True)
streamlit.write('<p style = "font-size:9px;">11.{}</p>'.format(generate_random_letters()),unsafe_allow_html = True)

line_numbers_and_their_font_sizes = {'1':152,'2':130,'3':108,'4':87,'6':65,'7':48,'8':33,'9':21,'10':15,'11':9}
                   
last_line_number_able_to_see = streamlit.text_input("which last line number you are able to see")

if streamlit.button('eye number'):
 if not int(last_line_number_able_to_see) > 11:
  eye_number = int(line_numbers_and_their_font_sizes.get(last_line_number_able_to_see)) / 20

  streamlit.write('your eye number is',eye_number)

 else:
  streamlit.write('exceeding maximum line number')


