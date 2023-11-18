import streamlit
import haversine

def get_distance(source_latitude,source_longitude,destination_latitude,destination_longitude):
 distance = int(haversine.haversine((source_latitude,source_longitude),(destination_latitude,destination_longitude),unit = 'm'))

 if distance >= 1000:
  distance = haversine.haversine((source_latitude,source_longitude),(destination_latitude,destination_longitude),unit = 'km')

  return str(distance) + ' ' + 'km'

 else:
  return str(distance) + ' ' + 'metre'


source_latitude = streamlit.text_input('Enter source latitude','source latitude')
source_longitude = streamlit.text_input('Enter source longitude','source longitude')

destination_latitude = streamlit.text_input('Enter destination latitude','destination latitude')
destination_longitude = streamlit.text_input('Enter destination longitude','destination longitude')

if streamlit.button('get distance'):
 distance = get_distance(float(source_latitude),float(source_longitude),float(destination_latitude),float(destination_longitude))

 streamlit.write(distance)
