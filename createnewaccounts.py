import mysql.connector
mydb = mysql.connector.connect(
host = 'localhost',
username = 'viraj',
password = 'sampulili',
database = 'viraj'
)
c = mydb.cursor()
x = input('create your password but password has to be 6 digits: ')
r = len(x)
if r == 6:
 c.execute('INSERT INTO passwords(password) VALUES("' + x + '"' + ')')
 mydb.commit()
else:
 print("your password is not 6 digits")
 
