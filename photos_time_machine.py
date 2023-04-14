import pyautogui

future_or_past = input('do you want to travel future or past? ')

if future_or_past == 'past':
 while True:
    pyautogui.press('PgDn')

if future_or_past == 'future':
 while True:
    pyautogui.press('PgUp')
