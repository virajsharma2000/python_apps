import requests
import webbrowser

def generate_diwali_wish(single_person_or_group):
 prompt = 'create a joyfull and reflecting diwali wish for a ' + single_person_or_group

 myobj = {"contents":[{"parts":[{"text":prompt}]}]}

 response = requests.post('https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyD1wjkjcVvOTqKHQdOuR-3NxhefycJrPAA', json = myobj)
 json_response = response.json()

 diwali_wish = json_response['candidates'][0]['content']['parts'][0]['text']
 
 return diwali_wish
