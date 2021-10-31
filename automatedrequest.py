import requests
import time
for i in range(11100000):
 s = requests.Session()
 r = s.get('http://localhost')
 print(r.text)
 time.sleep(1)

