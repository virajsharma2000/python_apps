import wikipedia
import webbrowser as web
import pyautogui as pg
import time
import socket
import requests
from twilio.rest import Client
import platform
import pyttsx3
from time import strftime
def whatsapp(time = int,message = str,sendto = str ) -> None:
    web.open('web.whatsapp.com/send?phone=' + sendto + '&text=' + message)
    pg.press("enter")
    time.sleep(time)
def info(topic = str) -> None:
    x = wikipedia.search(topic)
    print(x)
def ipaddress(host = str) -> None:
    r = socket.gethostbyname(host)
    print(r)
def HttpClient(address = str) -> None:
    s = requests.Session()
    r = s.get(address)
    print(r)
def twiliocall(fromphoneno = str,tophoneno = str,twiml = str) -> None:
    account_sid = "{account_sid}"
    auth_token = "_auth_token_"
    twilio = Client(account_sid, auth_token)
    call = twilio.calls.create(
    from_ = fromphoneno,
    to = tophoneno,
    twiml = twiml
    )
    print(call.sid)
def getcurrentos():
    r = platform.system()
    print(r)
def speecsynthesis(text = str) -> None:
    pyttsx3.speak(text)
def showtime(timeformat = str) -> None:
    strftime(timeformat)
