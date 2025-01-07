import requests
from dotenv import load_dotenv
import os

def summorize_school_written_work(text):
  load_dotenv()
  api_key = os.getenv("API_KEY")
  
  prompt = '{}\nsummorize text by extracting 4 points from the text of the answer, if the answer is too short, write the answer as it is, without changes, leave the answer as it is, then also do the same thing, and each point should be 1 line and put those points seperatly and mark each points as numbers and leave 1 line after each point, do not create para  or do not pack them into sentences or sentence from them  and do not summorize the questions, leave them as they are, but you have to write them'
  
  myobj = {"contents":[{"parts":[{"text":prompt.format(text)}]}]}

  questions_and_answers = requests.post('https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}', json = myobj) 

  return questions_and_answers.json()['candidates'][0]['content']['parts'][0]['text']
