from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout 

import random

def generate_phone_numbers(phone_number,how_many_phone_numbers):
        if len(phone_number) == 10:
         if phone_number.startswith('9') or phone_number.startswith('8') or phone_number.startswith('7'):
          phone_numbers = ''

          for i in range(int(how_many_phone_numbers)):
           numbers = list(phone_number[1:11])

           random.shuffle(numbers)

           numbers.insert(0,phone_number[0])
           
           for num in numbers:
            phone_numbers += num

           phone_numbers += '\n'

          layout = GridLayout(cols = 1, padding = 10)
          
          layout.add_widget(Label(text = phone_numbers))
          
          popup = Popup(title = 'PhoneNumberGenerator', 
                      content = layout, 
                      size_hint =(None, None), size =(1000, 1000))
          
          popup.open()

         else:
          layout = GridLayout(cols = 1, padding = 10)
         
          layout.add_widget(Label(text = 'your phone number is not starting with 9 or 8 or 7'))
         
          popup = Popup(title = 'PhoneNumberGenerator', 
                      content = layout, 
                      size_hint =(None, None), size =(1000, 1000))
         
          popup.open()    
          
          
        else:
         layout = GridLayout(cols = 1, padding = 10)
         
         layout.add_widget(Label(text = 'your phone number does not have 10 digits'))
         
         popup = Popup(title = 'PhoneNumberGenerator', 
                      content = layout, 
                      size_hint =(None, None), size =(1000, 1000))
         
         popup.open()    
          
          
class PhoneNumbersGeneratorApp(App):
    def build(self):
        boxlayout = BoxLayout(orientation = 'vertical')

        label1 = Label(text = 'Enter phone number')
        textbox1 = TextInput(size_hint = (.6,.35),pos_hint = {'x':.2,'y':.2})

        label2 = Label()

        label3 = Label(text = 'how many phone numbers to generate')
        textbox2 = TextInput(size_hint = (.6,.35),pos_hint = {'x':.2,'y':.2})

        label4 = Label(text = '\n')

        button = Button(text = 'generate phone numbers',size_hint = (.6,.35),pos_hint = {'x':.2,'y':.2})
        button.bind(on_press = lambda x:generate_phone_numbers(textbox1.text,textbox2.text))

        boxlayout.add_widget(label1)
        boxlayout.add_widget(textbox1)

        boxlayout.add_widget(label2)

        boxlayout.add_widget(label3)
        boxlayout.add_widget(textbox2)

        boxlayout.add_widget(label4)

        boxlayout.add_widget(button)
    
        return boxlayout


app = PhoneNumbersGeneratorApp()

app.run()



        
        
