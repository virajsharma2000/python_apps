import requests
import pywhatkit

def generate_diwali_wish(single_person_or_group):
 prompt = 'create a joyfull and reflecting diwali wish for a ' + single_person_or_group

 myobj = {"contents":[{"parts":[{"text":prompt}]}]}

 response = requests.post('https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyD1wjkjcVvOTqKHQdOuR-3NxhefycJrPAA', json = myobj)
 json_response = response.json()

 diwali_wish = json_response['candidates'][0]['content']['parts'][0]['text']
 
 return diwali_wish

def send_diwali_wish(phone_number_or_group_id):
 if phone_number_or_group_id.isdigit() and len(phone_number_or_group_id) == 10:
  if phone_number_or_group_id.startswith('9') or phone_number_or_group_id.startswith('8') or phone_number_or_group_id.startswith('7'):
   diwali_wish = generate_diwali_wish('single person')
   
   pywhatkit.sendwhatmsg_instantly('+91' + phone_number_or_group_id, diwali_wish)

  else:
   diwali_wish = generate_diwali_wish('group')

   pywhatkit.sendwhatmsg_to_group_instantly(phone_number_or_group_id, diwali_wish)

 else:
  diwali_wish = generate_diwali_wish('group')

  pywhatkit.sendwhatmsg_to_group_instantly(phone_number_or_group_id, diwali_wish)


