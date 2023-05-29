from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

import random

import time

player1_choice = ''
player2_choice = ''


def flip(event):
    global player1_choice
    global player2_choice
    
    head_and_tails = ['head','tails','head','tails','head','tails','head','tails']

    head_or_tails = random.choice(head_and_tails)

    if head_or_tails == player1_choice:
        popup = Popup(title = 'coinflip-1',content = Label(text = 'player1 wins {}'.format(head_or_tails)),size_hint = (.700,.200))

        popup.open()

    if head_or_tails == player2_choice:
        popup = Popup(title = 'coinflip-2',content = Label(text = 'player2 wins {}'.format(head_or_tails)),size_hint = (.700,.200))

        popup.open()
        

def choose_heads_for_player1(event):
    global player1_choice
    
    player1_choice += 'head'

def choose_tails_for_player1(event):
    global player1_choice

    player1_choice += 'tails'

def choose_heads_for_player2(event):
    global player2_choice

    player2_choice += 'head'


def choose_tails_for_player2(event):
    global player2_choice

    player2_choice += 'tails'

class CoinFlipApp(App):

    def build(self):
        
        layout = BoxLayout(orientation = 'vertical')
        
        label1 = Label(text = 'player1 choice')

        head1 = Button(text = 'head',size_hint = (.6,.35),pos_hint = {'x':.2,'y':.2})
        tails1 = Button(text = 'tails',size_hint = (.6,.35),pos_hint = {'x':.2,'y':.2})

        head1.bind(on_press = choose_heads_for_player1)
        tails1.bind(on_press = choose_tails_for_player1)

        label2 = Label(text = 'player2 choice')

        head2 = Button(text = 'head',size_hint = (.6,.35),pos_hint = {'x':.2,'y':.2})
        tails2 = Button(text = 'tails',size_hint = (.6,.35),pos_hint = {'x':.2,'y':.2})

        head2.bind(on_press = choose_heads_for_player2)
        tails2.bind(on_press = choose_tails_for_player2)

        

        flip_button = Button(text = 'flip',size_hint =(.6, .35),pos_hint = {'x':.2,'y':.2})

        flip_button.bind(on_press = flip)

        layout.add_widget(label1)

        layout.add_widget(head1)
        layout.add_widget(tails1)

        layout.add_widget(label2)
        
        layout.add_widget(head2)
        layout.add_widget(tails2)

        layout.add_widget(Label(text = '\n'))

        layout.add_widget(flip_button)

        return layout


app = CoinFlipApp()

app.run()

        

    

        

        
