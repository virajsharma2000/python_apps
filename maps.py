import webview

def createmap(maptitle,latitude,longitude,zoom):
 webview.create_window(maptitle,'https://www.google.com/maps/@' + latitude + ',' + longitude + ',' + ',' + zoom + 'z')
 webview.start()
