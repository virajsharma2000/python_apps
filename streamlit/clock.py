import streamlit as st
import time
import datetime

def draw_clock(time_in_second):
 angle_degrees = 0
 
 if int(time.strftime('%S')) > time_in_second:
  angle_degrees = (int(time.strftime('%S')) - time_in_second) * 6

 else:
  angle_degrees = (time_in_second - int(time.strftime('%S'))) * 6
   
 st.markdown('<svg height="200" width="200">'
                '<circle cx="100" cy="100" r="90" fill="none" stroke="black" stroke-width="3" />'
                '<line x1="100" y1="100" x2="100" y2="10" '
                'style="stroke:red;stroke-width:2" '
                'transform="rotate(angle_degrees), 100, 100)" />'
                '</svg>'.format(angle_degrees),unsafe_allow_html = True)


draw_clock(int(time.strftime('%S')))
