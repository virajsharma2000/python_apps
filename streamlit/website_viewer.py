import streamlit

def view_website(website_name):
 streamlit.write('<iframe src = "{}" width = 600 height = 600>'.format(website_name),unsafe_allow_html = True)

url = streamlit.text_input('url')

if streamlit.button('view website'):
 view_website(url)

