import streamlit

def show_website(website_url):
 streamlit.write('<iframe src = "{}">')


show_website('https://google.com')
