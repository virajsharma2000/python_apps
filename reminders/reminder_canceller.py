import mysql.connector

mydb = mysql.connector.connect(
host = 'localhost',
username = 'viraj',
password = 'pumpulili',
database = 'viraj'
)

attempts = 0

while True:
 reminder_id = int(input('Enter reminder id to cancel: '))

 attempts += 1

 print('attempts_number:'.format(attempts))

 c = mydb.cursor()
 c.execute('select reminder_id from reminders')

 r = c.fetchall()

 for records in r:
    if reminder_id in records:
        c.execute('update set status="cancelled" where reminder_id={}'.format(reminder_id))

    else:
        print('Error:reminder id not found')

 if attempts == 3:
     break
    print("now you don't have any other try")

        

