from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

import random


phone_numbers = ''

def generate_phone_numbers(phone_number,how_many_phone_numbers):
         global phone_numbers

         try:
          if len(phone_number) == 8 or len(phone_number) == 10:
           int(phone_number)
         
           numbers = []

           for nums in phone_number:
            numbers.append(nums)
         
           for i in range(int(how_many_phone_numbers)):
            phone_num = ''

            for x in range(len(phone_number)):
             num = random.choice(numbers)

             phone_num += num


            phone_numbers += phone_num + '\n'     

           Popup(title = 'PhoneNumberGenerator',content = Label(text = phone_numbers)).open()

           phone_numbers = ''
 
         except ValueError:
           pass
         
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



        
        
