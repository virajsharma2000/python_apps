import webbrowser as web
import pyautogui as pg
import time
import smtplib
def automaticwhatsapp():
 print("warning! don't open this app again if whatsapp is waiting to send a message")
 x = input("Enter phone number with country code: ")
 y = input("Enter message: ")
 z = int(input("Enter time in seconds after whatsapp message would be sent: "))
 web.open("https://web.whatsapp.com/send?phone=" + x + "&text=" + y)
 time.sleep(z)
 pg.press("enter")
def automatedmail():
 session = smtplib.SMTP('smtp.gmail.com',587)
 session.starttls()
 session.login('your email','your password)
 session.sendmail('your email address',input("Enter to email address: "),input("Enter email message: "))
 session.quit()
def automatedmailreminder():
 x = int(input("Enter time in hours: "))
 y = int(input("Enter time in minutes: "))
 z = int(input("Enter time in seconds: "))
 n = input("Enter text message to remind in email: ")
 s = input("Enter whome to send the email: ")
 i = int(input("Enter how much times to send mails: "))
 t = int(input("Enter how much seconds to stop then send countinuesly: "))
 while True:
  if time.localtime().tm_hour == x and time.localtime().tm_min == y and time.localtime().tm_secs == z:
   break
 for x in range(i):
  session = smtplib.SMTP('smtp.email.com',587)
  session.starttls()
  session.login(','your password')
  session.sendmail('your email address',s,n)
  session.quit()
  time.sleep(t)
x = input("it has three functions Enter which automated function do you want autimaticwhatsapp,automatedmail or automatedmailreminder: ")
if x == 'automaticwhatsapp':
 automaticwhatsapp()
if x == 'automatedmail':
 automatedmail()
if x == 'automatedmailreminder':
 automatedmailreminder()
 
