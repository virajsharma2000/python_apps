import requests

class SIMS:
 def __init__(self,token):
  self.token = token
 def send_message(self,from_firstname = None,from_lastname = None,to_firstname = None,to_lastname = None,your_message = None):
  if self.token == '0101010101010101010101010100101010101010':
     request = requests.get('http://192.168.1.252:8080/messages/{}/{}?your_firstname={}&your_lastname={}&message={}'.format(
     to_firstname,
     to_lastname,
     from_firstname,
     from_lastname,
     your_message
     ))

     return request.text
    
  else:
    raise Exception('invalid token id')


def show_token_id():
     return '0101010101010101010101010100101010101010'
    
