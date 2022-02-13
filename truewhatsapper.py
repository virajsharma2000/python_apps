import mysql.connector
import webbrowser
mydb = mysql.connector.connect(
host = 'localhost',
username = 'viraj',
password = 'sampulili',
database = 'viraj'
)
c = mydb.cursor()
phone = input("phone number with country code: ")
c.execute('select name from whatsappcontacts WHERE phone=' + phone)
r = c.fetchall()
for x in r:
 i = x[0]
 print(i)
 x = input('do you want to chat: ')
 if x == 'yes':
  webbrowser.open("https://web.whatsapp.com/send?phone=" + phone)
 if x == 'no':
  exit()
  
