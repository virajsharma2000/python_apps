import requests

def detect_emotion(text):
  prompt = 'can you get emotion in the text given below, do not give me explaination, just name of emotion in single word' + '\n' + text
  
  myobj = {"contents":[{"parts":[{"text":prompt}]}]}

  response = requests.post('https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyD1wjkjcVvOTqKHQdOuR-3NxhefycJrPAA', json = myobj) 

  return response.json()['candidates'][0]['content']['parts'][0]['text']


detect_emotion('I am surprised')
