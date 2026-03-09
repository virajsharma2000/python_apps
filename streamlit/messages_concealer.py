import streamlit as st
import requests
import sqlite3
import datetime
import random
import string

db = sqlite3.connect('messages_mapped_with_orignal.db')

def hide_message(conversation_id, msg, grade, study_theme):
 db.cursor()
 records = db.execute(f'SELECT * FROM {conversation_id}')
 messages = []
 message_count = 1

 for message in records.fetchall():
  if message_count % 2 == 0:
   messages.append(('friend2', message[2], 'sent at - ' + message[0]))

  else:
   messages.append(('friend1', message[2], 'sent at - ' + message[0]))

 print(messages)

 if messages:
  prompt = f"you are a friend chatting with other friend. Generate a message based on previous conversation {messages}. Reply as 1 kid replies to friend, just reply with a simple text without including anything fun"
  
 else:
  prompt = f"you are a friend chatting with other friend. Generate a message starting a normal {study_theme} conversation of class {grade}th without including anything fun. Reply as 1 kid replies to friend, just reply with a simple text"

 payload = {
  "model": "sarvam-m",
  "messages": [
    {"role": "user", "content": prompt}
  ],
  "temperature": 0.97,
  "max_tokens": 150
}
 
 response = requests.post("https://api.sarvam.ai/v1/chat/completions", headers = {
    "api-subscription-key": "sk_ma7dcpkt_6lF8m4QMYZM1vcEm16kFzd76",
    "Content-Type": "application/json"  # usually needed for APIs
}, json = payload)

 generated_message = response.json()['choices'][0]['message']['content'].replace('<think>\n ', '').replace('"', '')

 db.execute(f'INSERT INTO {conversation_id}(datetime, orignal_message, mapped_message) VALUES(?, ?, ?)', (datetime.datetime.now().strftime('%Y-%B -%d %I:%M:%S'), msg, generated_message))
 db.commit()

 return generated_message

def get_orignal_message(conversation_id, generated_message):
 db.cursor()
 records = db.execute(f'SELECT * FROM "{conversation_id}" WHERE mapped_message=?', (generated_message,))
 message = records.fetchall()
 
 return message[0][1]

def generate_id():
 id = ''.join(random.choice(string.ascii_letters) for i in range(9))
 db.execute(f'CREATE TABLE {id}(datetime VARCHAR(100) NOT NULL, orignal_message VARCHAR(10000) NOT NULL, mapped_message VARCHAR(10000) NOT NULL)')

 return id


st.header('HIDE MESSAGES EASILY FROM YOUR PARENTS, THEY WOULD NEVER DOUBT YOU HAHAHAHA!!!! 😈')

st.subheader('IF YOU WANT TO CHAT WITH YOUR FRIENDS USING A SECRET ID DO THIS, JUST 1 CLICK AWAY HAHAHAHA - ')
if st.button('Get Your conversation ID'):
 id = generate_id()
 st.subheader('your id is - ' +  id + ' save it in your file and share it with your friend')

st.subheader('IF YOU WANT TO HIDE YOUR MESSAGE DO THIS - ')

conversation_id = st.text_input('Enter conversation id')
orignal_message = st.text_input('Enter orignal message')
grade = st.text_input('in which grade you are in')
study_theme = st.text_input('Enter study theme for ex. Exams, Homework, Project, Holiday Homework')

if st.button('Hide Message'):
 msg = hide_message(conversation_id, orignal_message, grade, study_theme)
 st.write('replaced message to send in whatsapp - ' + msg)

st.subheader('IF YOU WANT TO SEE THE ORIGNAL MESSAGE SENT BY YOUR FRIEND, DO THIS - ')

conversation_id = st.text_input('Enter your conversation id')
generated_message = st.text_input('Enter the message which your friend sent in whatsapp')

if st.button('See'):
 orignal_message = get_orignal_message(conversation_id, generated_message)
 st.write('orignal message sent by your friend - ' + orignal_message)

