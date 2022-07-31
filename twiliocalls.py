from twilio.rest import Client
import tkinter
import easygui

account_sid = '<YOUR_ACCOUNT_SID>'
auth_token = '<YOUR_AUTH_TOKEN>'

twilio = Client(account_sid,auth_token)

tophone = easygui.enterbox('whome you want to call enter the phone number here:')
newtwiml = easygui.textbox()

call = twilio.calls.create(
from_ = '+13213513640',
to = tophone,
twiml = newtwiml
)

r = tkinter.Tk()

r.title('call status')
r.geometry('200x300')

def call_status():
 callstatus = twilio.calls(call.sid).fetch().status
 l.config(text = callstatus)
 l.after(1000,call_status)


l = tkinter.Label(r,font = ('courier'))
call_status()
l.pack()

r.mainloop()
