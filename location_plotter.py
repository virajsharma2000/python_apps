import what3words
import webview

def read_cookies(window):
    cookies = window.get_cookies()
    for c in cookies:
     c.output()

def plot_location(latitude,longitude):
 what3words_geocoder = what3words.Geocoder('UQFJQOOY')

 json_response = what3words_geocoder.convert_to_3wa(what3words.Coordinates(latitude,longitude))
 three_words = json_response['words']

 window = webview.create_window('my location','https://what3words.com/{}'.format(three_words))
 webview.start(read_cookies,window,private_mode = False)


lat = input('latitude: ')
lng = input('longitude: ')

plot_location(lat,lng)

