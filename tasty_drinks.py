import mysql.connector
import datetime

def order(first_name,last_name,which_drink_to_order,flat_number,society_name,floor_number):
 name = first_name + ' ' + last_name
 order_time = datetime.datetime.now().strftime('%d %B,%A %Y %I:%M %P')

 drinks_list = ['sting energy','charged','monster','Redline xtreme']

 if which_drink_to_order in drinks_list:
    mydb = mysql.connector.connect(
    host = '127.0.0.1:3306',
    username = 'u568486805_ordering_drink',
    password = 'order24pumpulili',
    database = 'u568486805_order'
    )

    c1 = mydb.cursor()
    c1.execute(
        'INSERT INTO orders(name,flat_number,floor_number,society_name,which_drink_to_order,order_status,order_time) VALUES({},{},{},"{}","{}","{}")'.format(
        name,
        flat_nuber,
        floor_number,
        society_name,
        'ordered successfully!!',
        order_time
        )
        )

    mydb.commit()

    c2 = mydb.cursor()
    c2.execute('select order_id from orders WHERE name={}'.format(name))
    r = c2.fetchall()

    for record in r:
        order_id = record[0]
        print('ordered successfully!! with order id:{}'.format(order_id))

 else:
     print('ERROR :( -> drink is not avelabel')


def drinks_menu():
     print('sting energy   Rs.200')
     print('charged        Rs.500')
     print('monster        Rs.800')
     print('Redline xtreme Rs.900')


drinks_menu()

print()

first_name = input('Enter first name: ')
last_name = input('Enter last name: ')

flat_number = int(input('Enter your flat number: '))
floor_number = int(input('Enter your floor number: '))
society_name = input('Enter your society name: ')
which_drink_to_order = input('Enter which drink to order: ')

order(first_name,last_name,which_drink_to_order,flat_number,society_name,floor_number)
