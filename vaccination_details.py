import mysql.connector
import datetime

mydb = mysql.connector.connector(
host = 'localhost',
username = 'viraj',
password = 'pumpulili',
database = 'viraj'
)

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

name = first_name + ' ' + last_name

c = mydb.cursor()

vaccinated_people_list = []

c.execute('select * from vaccinated_people where date={}'.format(datetimedatetime.now().strftime('%B - %d - %Y')))

r = c.fetchall()

for records in r:
    first_name = records[0]
    last_name = records[1]

    vaccinated_people_list.append(first_name + ' ' + last_name)

number_of_people_vaccinated = len(vaccinated_people_list)

print('today {} people were vaccinated\n\n')

if name in vaccinated_people_list:
    print('congratulations you are also vaccinated today!!\nbut still follow the following rules:\n1.wear mask\n2.social distance\n3.sanitize your hands and your courier\n4.wash hand with soap and water')

else:
 print('follow the following rules:\n1.wear mask\n2.social distance\n3.sanitize your hands and your courier\n4.wash hand with soap and water')    
