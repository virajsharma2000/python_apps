import mysql.connector
import easygui

mydb = mysql.connector.connect(
host = 'localhost',
username = 'viraj',
password = 'pumpulili',
database = 'viraj'
)

c = mydb.cursor()

first_name = easygui.enterbox('first name')
last_name = easygui.enterbox('last name')

gender = easygui.enterbox('gender - male or female')
age = int(easygui.enterbox('age'))
description = easygui.textbox('description')

c.execute('INSERT INTO members(first_name,last_name,gender,age,description) VALUES("{}","{}","{}",{},"{}")'.format(first_name,last_name,gender,age,description))

mydb.commit()
