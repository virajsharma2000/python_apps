import streamlit as st

digipin_grid = [
    ['F', 'C', '9', '8'],
    ['J', '3', '2', '7'],
    ['K', '4', '5', '6'],
    ['L', 'M', 'P', 'T']
]
  
bounds = {
    'minLat': 2.5,
    'maxLat': 38.5,
    'minLon': 63.5,
    'maxLon': 99.5
}

def latlng_to_digipin(lat, lon):
 maxlat = bounds['maxLat']
 maxlon = bounds['maxLon']
 minlat = bounds['minLat']
 minlon = bounds['minLon']
 
 if lat > maxlat or lat < minlat:
  raise ValueError('latitude out of range') 
 
 elif lon > maxlon or lon < minlon:
  raise ValueError('longitude out of range')

 digipin = ''

 for i in range(10):
  latdiv = (maxlat - minlat) / 4
  londiv = (maxlon - minlon) / 4

  row =  3 - int((lat - minlat) / latdiv)
  col = int(int((lon - minlon) / londiv))

  row = max(0, min(row, 3))
  col = max(0, min(col, 3))

  digipin += digipin_grid[row][col]

  maxlat = minlat + latdiv * (4 - row)
  minlat = minlat + latdiv * (3 - row)
  
  minlon = minlon + londiv * col
  maxlon = minlon + londiv

 return digipin[:3] + '-' + digipin[3:6] + '-' + digipin[6:10]


st.title('get your house coordinates to digipin if you forgotten it')

lat = st.text_input('Enter latitude')
lon = st.text_input('Enter longitude')

if st.button('Get Digipin'):
 digipin = latlng_to_digipin(float(lat), float(lon))

 st.subheader('your digipin: ' + str(digipin))







