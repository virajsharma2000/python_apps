import easygui
import tkinter
import webbrowser


r = tkinter.Tk()

r.title('chat whatsapp')


def chatwhatsapp():
 x = easygui.enterbox('enter phone number with country code')
 webbrowser.open('https://web.whatsapp.com/send?phone=' + x)

def sendtext():
 x = easygui.enterbox('enter phone number with country code')
 y = easygui.enterbox('enter text message or link')
 webbrowser.open('https://web.whatsapp.com/send?phone=' + x + '&text=' + y)

tkinter.Button(r,text = 'chat with someone in whatsapp',command = chatwhatsapp).grid(row = 21)
tkinter.Button(r,text = 'send text or link in whatsapp',command = sendtext).grid(row = 22)

r.mainloop()
 
 
