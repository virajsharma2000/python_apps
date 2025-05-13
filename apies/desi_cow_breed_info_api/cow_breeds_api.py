from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/cow_breed')

def get_info_of_cow_breed():
 breed_name = request.values.get('breed_name')

 with open('desi_cow_breeds_full_58.json') as f:
  cow_breeds_info_json = f.read()
  json_of_cow_breeds = json.loads(cow_breeds_info_json)

  for cow_breed_info in json_of_cow_breeds['desiCowBreeds']:
   if cow_breed_info['name'] == breed_name.capitalize():
    return cow_breed_info
   

if __name__ == '__main__':
 app.run(host = '127.0.0.1', port = 8080)

 