import requests

def summorize_school_written_work(text):
  prompt = '{}\nremove some words from answers of the questions of the text and summorize it in 4 lines and 20 charecters, and do not make answer look too different and return the questions as they were, with no change, and the answer should not look too different, and return answer in points, and very slight different'
  
  myobj = {"contents":[{"parts":[{"text":prompt.format(text)}]}]}

  questions_and_answers = requests.post('https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyD1wjkjcVvOTqKHQdOuR-3NxhefycJrPAA', json = myobj) 

  return questions_and_answers.json()['candidates'][0]['content']['parts'][0]['text']
