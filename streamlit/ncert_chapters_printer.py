from bs4 import BeautifulSoup
import requests
import streamlit as st

def chapters(grade, book_title):
 if grade >= 3 and grade <= 12:
  book_title = book_title.lower().replace(' ', '-')

  if book_title.split('-')[0] == 'social' and book_title.split('-')[1] == 'science':
   url = f'https://www.vedantu.com/ncert-solutions/ncert-solutions-class-{grade}-{book_title}'

  else:
   url = f'https://www.vedantu.com/ncert-books/ncert-books-class-{grade}-{book_title}'

  print(url)
   
  response = requests.get(url)
  source_code = response.text

  soup = BeautifulSoup(source_code, 'html.parser')

  chapters = []
 
  for link in soup.find_all('a'):
   if link.text.split() and link.text.split()[0] == 'Chapter' and link.text.split()[1][0].isdigit():
    chapters.append(link.text.replace('Solutions', ''))

  return chapters


grade = st.text_input('Enter grade: ')
book_title = st.selectbox('select book title', ('Physics', 'Chemistry', 'Biology', 'Science', 'Maths', 'Social science resources and development', 'social science our pasts 3', 'Hindi vasant'))

if st.button('Print Chapters'):
 for chapter in chapters(int(grade), book_title):
  st.write(chapter)
 
