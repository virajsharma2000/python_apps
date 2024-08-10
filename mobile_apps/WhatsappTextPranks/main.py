from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout

import webbrowser
import random

def send_flipped_text(text):
 upside_down_unicode = [
    0x0250, 0x0071, 0x0254, 0x0070, 0x01DD, 0x025F, 0x0253, 0x0265, 0x0131, 0x027E, 0x029E, 0x006C, 0x026F, 0x0075,
    0x006F, 0x0064, 0x0062, 0x0279, 0x0073, 0x0287, 0x006E, 0x028C, 0x028D, 0x0078, 0x028E, 0x007A, 0x2200, 0x0071,
    0x2183, 0x0070, 0x018E, 0x2132, 0x2141, 0x0048, 0x0049, 0x017F, 0x029E, 0x02E5, 0x0057, 0x004E, 0x004F, 0x0500,
    0x0051, 0x1D1A, 0x0053, 0x22A5, 0x2229, 0x039B, 0x004D, 0x0058, 0x2144, 0x005A
    ]

 letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Z'
           ]
 
 upside_down_text = ''

 for letter in text:
  if letter in letters:
   upside_down_text += chr(upside_down_unicode[letters.index(letter)])

  else:
   upside_down_text += letter

 flipped_text = upside_down_text[::-1]

 webbrowser.open('https://api.whatsapp.com/send/?text=' + flipped_text)

def send_upside_down_text(text):
 upside_down_unicode = [
    0x0250, 0x0071, 0x0254, 0x0070, 0x01DD, 0x025F, 0x0253, 0x0265, 0x0131, 0x027E, 0x029E, 0x006C, 0x026F, 0x0075,
    0x006F, 0x0064, 0x0062, 0x0279, 0x0073, 0x0287, 0x006E, 0x028C, 0x028D, 0x0078, 0x028E, 0x007A, 0x2200, 0x0071,
    0x2183, 0x0070, 0x018E, 0x2132, 0x2141, 0x0048, 0x0049, 0x017F, 0x029E, 0x02E5, 0x0057, 0x004E, 0x004F, 0x0500,
    0x0051, 0x1D1A, 0x0053, 0x22A5, 0x2229, 0x039B, 0x004D, 0x0058, 0x2144, 0x005A
    ]

 letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Z'
           ]

 upside_down_text = ''

 for letter in text:
  if letter in letters:
   upside_down_text += chr(upside_down_unicode[letters.index(letter)])

  else:
   upside_down_text += letter

 webbrowser.open('https://api.whatsapp.com/send/?text=' + upside_down_text)

def send_reversed_text(text):
 reversed_text = text[::-1]

 webbrowser.open('https://api.whatsapp.com/send/?text=' + reversed_text)

def send_blank_text(event):
 blank_text = ''

 columns = random.randint(10,20)
 rows = random.randint(10,20)

 for col in range(columns):
  blank_text += '\u2066'
  blank_text += '\n'

 webbrowser.open('https://api.whatsapp.com/send/?text=' + blank_text)

class WhatsappTextPranks(App):
 def build(self):
  layout = BoxLayout(orientation = 'vertical')

  label = Label(text = 'Enter text, if sending blank text, you do not to fill this textbox')
  message = TextInput(size_hint = (.6,.33),pos_hint = {'x':.2,'y':.2})

  send_flipped_text_button = Button(text = 'Send Flipped Text',size_hint = (.6,.33),pos_hint = {'x':.2,'y':.2})
  send_upside_down_text_button = Button(text = 'Send Upsidedown Text',size_hint = (.6,.33),pos_hint = {'x':.2,'y':.2})
  send_reversed_text_button = Button(text = 'Send Reversed Text',size_hint = (.6,.33),pos_hint = {'x':.2,'y':.2})
  
  send_blank_text_button = Button(text = 'Send Blank Text',size_hint = (.6,.33),pos_hint = {'x':.2,'y':.2})

  send_flipped_text_button.bind(on_press = lambda x:send_flipped_text(message.text))
  send_upside_down_text_button.bind(on_press = lambda x:send_upside_down_text(message.text))
  send_reversed_text_button.bind(on_press = lambda x:send_reversed_text(message.text))

  send_blank_text_button.bind(on_press = send_blank_text)

  layout.add_widget(label)
  layout.add_widget(message)
  
  layout.add_widget(send_flipped_text_button)
  layout.add_widget(send_upside_down_text_button)
  layout.add_widget(send_reversed_text_button)

  layout.add_widget(send_blank_text_button)

  return layout


app = WhatsappTextPranks()

app.run()
  
  
