from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout

from plyer import vibrator

def vibrate(duration):
 if vibrator.exists():
  vibrator.vibrate(int(duration))


class Vibrator(App):
 def build(self):
  layout = BoxLayout(orientation = 'vertical')

  label = Label(text = 'duration of vibration in seconds')
  duration = TextInput(size_hint = (.6,.33),pos_hint = {'x':.2,'y':.2})
  
  button = Button(text = 'Vibrate',size_hint = (.6,.33),pos_hint = {'x':.2,'y':.2})
  button.bind(on_press = lambda x: vibrate(duration.text))

  layout.add_widget(label)
  layout.add_widget(duration)

  layout.add_widget(button)

  return layout


app = Vibrator()
app.run()
