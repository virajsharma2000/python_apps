# my app for checking compas direction

import streamlit
import pycompas

source_latitude = streamlit.text_input('Enter source latitude','source latitude')
source_longitude = streamlit.text_input('Enter source longitude','source longitude')
destination_latitude = streamlit.text_input('Enter destination latitude','destination latitude')
destination_longitude = streamlit.text_input('Enter destination longitude','destination longitude')

if streamlit.button('get compas direction'):
 compas_direction = pycompas.get_compas_direction([source_latitude,source_longitude],[destination_latitude,destination_longitude])

 streamlit.write(compas_direction)
