import requests

name = input("Enter your name: ")

def chat(user):
 while True:
  message = input('message: ')
  print('you: ' + message)
  r = requests.get('http://192.168.1.19:8080/messages?name=' + user + '&message=' + message)
  print(r.text)

if name == '':
    print("you cannot goto chat if you don't enter your name")

else:
 chat(name)
