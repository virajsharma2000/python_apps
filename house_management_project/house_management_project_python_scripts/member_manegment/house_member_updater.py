import mysql.connector
import easygui

mydb = mysql.connector.connect(
host = 'localhost',
username = 'viraj',
password = 'pumpulili',
database = 'viraj'
)

c = mydb.cursor()

member_id = int(easygui.enterbox('member id'))


first_name = easygui.enterbox('first name')
last_name = easygui.enterbox('last name')

gender = easygui.enterbox('gender')
age = easygui.enterbox('age')
description = easygui.textbox('description')

c.execute('UPDATE members SET first_name="{}",last_name="{}",gender="{}",age={},description="{}" WHERE member_id={}'.format(
    first_name,
    last_name,
    gender,
    age,
    description,
    member_id
    )

    )

mydb.commit()
