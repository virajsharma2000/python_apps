import requests


from_firstname = input('Enter your first name: ')
from_lastname = input('Enter your last name: ')
to_firstname = input('Enter first name whome you want to send message: ')
to_lastname = input('Enter last name whome you want to send message: ')
your_message = input('Enter your message: ')



client = requests.get('http://192.168.1.252:8080/messages/{}/{}?your_firstname={}&your_lastname={}&message={}'.format(
to_firstname,
to_lastname,
from_firstname,
from_lastname,
your_message
))

print(client.text)
    
