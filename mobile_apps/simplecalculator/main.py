from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.uix.popup import Popup


def calculate(expression):
    try:
      if '+' in expression or '-' in expression or '*' in expression or '/' in expression or '(' in expression or ')' in expression or expression.isdigit():
         answer = eval(expression)

         Popup(title = 'simple calculator',content = Label(text = str(answer)),size_hint = (.900,.200)).open()

      else:
         Popup(title = 'simple calculator',content = Label(text = 'Error'),size_hint = (.900,.200)).open()

    except:
         Popup(title = 'simple calculator',content = Label(text = 'Error'),size_hint = (.900,.200)).open()
         


class SimpleCalculatorApp(App):
    def build(self):
        boxlayout = BoxLayout(orientation = 'vertical')

        label = Label(text = 'Enter your expression below in your text box')
        textbox = TextInput(size_hint = (.6,.2),pos_hint = {'x':.2,'y':.2})

        button = Button(text = 'calculate',size_hint = (.6,.2),pos_hint = {'x':.2,'y':.2})

        button.bind(on_press = lambda x:calculate(textbox.text))

        boxlayout.add_widget(label)
        boxlayout.add_widget(textbox)

        boxlayout.add_widget(Label())

        boxlayout.add_widget(button)

        return boxlayout


app = SimpleCalculatorApp()

app.run()
    
