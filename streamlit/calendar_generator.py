import calendar
import datetime
import streamlit as st

year = int(datetime.datetime.now().strftime('%Y'))

def create_calendar():
 global year

 cal = calendar.calendar(2021)

 return cal

def move_to_next_year():
 global year

 year += 1


cal = create_calendar()

if st.button('year'):
 move_to_next_year()

 cal = create_calendar()

 st.write(cal)
