import mysql.connector

mydb = mysql.connector.connect(
host = 'localhost',
username = 'viraj',
password = 'pumpulili',
database = 'viraj'
)

c = mydb.cursor()
c.execute('select * from reminders')

r = c.fetchall()

if any(r) == True:
 for records in r:
        print('remind_for: {}'.format(records[1]))
        print('reminder_time_hours: {}'.format(records[2]))
        print('remimder_time_minutes: {}'.format(records[3]))
        print('reminder_am_or_pm: {}'.format(records[4]))
        print('reminder_status: {}'.format(records[5]))

        print()

else:
    print("you don't have any reminders \u2205")
        
