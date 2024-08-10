from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout

import random
import webbrowser
import time

def trigger_whatsapp(phone_num):
 if phone_num.text != 'already tapped':
  webbrowser.open('https://api.whatsapp.com/send/?phone=' + phone_num.text.split(' - ')[0])
  phone_num.text = 'already tapped'

def generate_phone_numbers(how_many_phone_numbers):
 phone_numbers = ''

 for i in range(int(how_many_phone_numbers)):
  numbers = ['1','2','3','4','5','6','7','8','9']

  random.shuffle(numbers)

  phone_numbers += random.choice(['9','8','7'])
  
  for num in numbers:
   phone_numbers += num

  if i + 1 < int(how_many_phone_numbers):
   phone_numbers += ','

 layout = BoxLayout(orientation = 'vertical')
   
 for phone_num in phone_numbers.split(','):
  button = Button(text = phone_num + ' - ' + 'tap me',size_hint = (.6,.35),pos_hint = {'x':.2,'y':.2})
  button.bind(on_press = lambda phone_num:trigger_whatsapp(phone_num))

  layout.add_widget(button)

 popup_window = Popup(title = 'PhoneNumberGenerator',content = layout)
 popup_window.open()


class PhoneNumbersGeneratorApp(App):
    def build(self):
        boxlayout = BoxLayout(orientation = 'vertical')

        label3 = Label(text = 'how many phone numbers to generate')
        phone_number = TextInput(size_hint = (.6,.35),pos_hint = {'x':.2,'y':.2})

        label4 = Label(text = '\n')

        button = Button(text = 'generate phone numbers',size_hint = (.6,.35),pos_hint = {'x':.2,'y':.2})
        button.bind(on_press = lambda x:generate_phone_numbers(phone_number.text))

        boxlayout.add_widget(label3)
        boxlayout.add_widget(phone_number)

        boxlayout.add_widget(label4)

        boxlayout.add_widget(button)
    
        return boxlayout


app = PhoneNumbersGeneratorApp()

app.run()



        
        
