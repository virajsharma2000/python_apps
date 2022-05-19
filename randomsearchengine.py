import webview
import random
import mysql.connector

user = input('name: ')

mydb = mysql.connector.connect(host = 'localhost',username = 'viraj',password = 'sampulili',database = 'viraj')
c = mydb.cursor()
c.execute('select count(*) from users WHERE name="' + user + '"')
r = c.fetchall()

for record in r:
 username = record[0]

def webbrowseraccess(name):
 searchengines = ['https://google.com','https://duckduckgo.com']

 webview.create_window('random search engine is using by: ' + name,random.choice(searchengines))
 webview.start()


if username == 0:
 print('wrong name! pleas goto app called randomsearchenginesignup app and sign up there')

else:
 webbrowseraccess(user)

