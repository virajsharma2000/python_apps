import webbrowser
import random

message = input('Enter text: ')

reversed_message = ''

letter_array = []

for msg in message:
    letter_array += msg

index = len(letter_array) - 1

for x in range(len(letter_array)):
    letter = letter_array[index]

    index -= 1

    reversed_message += letter

webbrowser.open('https://web.whatsapp.com/send?text={}'.format(phone_nums,reversed_message))

    
    
