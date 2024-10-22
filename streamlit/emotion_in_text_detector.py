import requests

def detect_emotion(text):
  prompt = 'can you get emotion in the text given below' + '\n' + text
  
  myobj = {"contents":[{"parts":[{"text":prompt}]}]}

  questions_and_answers = requests.post('https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyD1wjkjcVvOTqKHQdOuR-3NxhefycJrPAA', json = myobj) 

  return questions_and_answers.json()['candidates'][0]['content']['parts'][0]['text']


