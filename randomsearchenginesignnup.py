import mysql.connector

username = input("name: ")

mydb = mysql.connector.connect(host = 'localhost',username = 'viraj',password = 'sampulili',database = 'viraj')
c = mydb.cursor()
c.execute('INSERT INTO users(name) VALUES("' + username + '"' + ')')
mydb.commit()
