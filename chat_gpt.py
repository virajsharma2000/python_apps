import openai
import speech_recognition as sr

choice = input('do you want to ask question text or speech: ')
question =""
if choice == 'speech':
 r = sr.Recognizer()

 with sr.Microphone(device_index=0) as source:
    audio = r.listen(source, phrase_time_limit=5)

 question_json = r.recognize_google(audio)
 

if choice == 'text':
    print()
    
    question = input('Enter your question: ')


openai.api_key = 'YOUR_OPENAI_API_KEY'

answer = openai.Completion.create(
                                model = 'text-davinci-003',
                                prompt = question
                                )['choices'][0]['text']

print('\nanswer found! answer is written below {}'.format(answer))
