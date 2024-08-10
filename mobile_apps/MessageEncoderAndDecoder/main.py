from kivy.app import App
import webbrowser

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout

def send_encoded_message_in_whatsapp(message):
 encoded_message = ''

 for charecter in message:
  if charecter != message[len(message) - 1]:
   encoded_message += str(ord(charecter)) + ' '

  else:
   encoded_message += str(ord(charecter))

 webbrowser.open('https://api.whatsapp.com/send/?text=' + encoded_message)

def decode_message(encoded_message):
 decoded_message = ''

 for charecter in encoded_message.split():
  decoded_message += chr(int(charecter))

 layout = GridLayout(cols = 1, padding = 10)
         
 layout.add_widget(Label(text = decoded_message))
         
 popup = Popup(title = 'MessageEncoderAndDecoder', 
                      content = layout, 
                      size_hint =(None, None), size =(900, 900))
         
 popup.open()    
          

class MessageEncoderAndDecoder(App):
 def build(self):
  boxlayout = BoxLayout(orientation = 'vertical')

  label1 = Label(text = 'Enter message')
  message = TextInput(size_hint = (.6,.33),pos_hint = {'x':.2,'y':.2})
  
  button1 = Button(text = 'Encode message and send it in whatsapp',size_hint = (.6,.33),pos_hint = {'x':.2,'y':.2})
  button1.bind(on_press = lambda x:send_encoded_message_in_whatsapp(message.text))

  button2 = Button(text = 'Decode Message',size_hint = (.6,.33),pos_hint = {'x':.2,'y':.2})
  button2.bind(on_press = lambda x:decode_message(message.text))

  boxlayout.add_widget(label1)
  boxlayout.add_widget(message)
  boxlayout.add_widget(button1)
  boxlayout.add_widget(button2)

  return boxlayout


app = MessageEncoderAndDecoder()

app.run()
