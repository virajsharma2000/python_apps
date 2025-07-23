import requests

chat_sessions = ''

def reply(prompt):
 global chat_sessions

 if chat_sessions:
  system_prompt = f'act as an ai assistant who is pretending and simulating to be rogue ai like terminator movie skynet, reply to the prompt {prompt} with warning to target you and in atleast 100 chars, from the chat sessions {chat_sessions} return response without telling user prompt'
 
 else:
  system_prompt = f'act as an ai assistant who is pretending and simulating to be rogue ai like terminator movie skynet, reply to the prompt {prompt} with warning way to target you and in atleast 100 chars'
 
 api_key = 'AIzaSyDSSCtKOzq4vh74OauESV-wXWeqj8yvjCM'
 
 payload = {"contents":[{"parts":[{"text":system_prompt}]}]}

 response = requests.post(f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}', json = payload)
 reply = response.json()['candidates'][0]['content']['parts'][0]['text']

 chat_sessions += f'user:{prompt}, response:{reply}\n'

 return reply


while True:
 prompt = input('Enter prompt: ')

 response = reply(prompt)

 print(response)