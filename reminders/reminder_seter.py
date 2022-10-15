import mysql.connector

mydb = mysql.connector.connect(
host = 'localhost',
username = 'viraj',
password = 'pumpulili',
database = 'viraj'
)

c = mydb.cursor()

remind_for = input('what should I remind for: ')
reminder_time_hours = int(input('Enter reminder time in hours: '))
reminder_time_minutes = int(input('Enter reminder time in minutes: '))
reminder_time_am_or_pm = input('am or pm: ')

print('1.reapeted')
print('2.once')

reminder_status = input('choose reminder status from above: ')

if reminder_status == '1':
 reminder_status = 'pending'
 c.execute(
    'INSERT INTO reminders(remind_for,reminder_time_hours,reminder_time_minutes,reminder_time_am_or_pm,reminder_status) VALUES("{}",{},{},"{}","{}")'.format(
        remind_for,
        reminder_time_hours,
        reminder_time_minutes,
        reminder_time_am_or_pm,
        reminder_status
        )
    )

 mydb.commit()

if reminder_status == '2':
    reminder_status = 'reapeted'
    c.execute(
    'INSERT INTO reminders(remind_for,reminder_time_hours,reminder_time_minutes,reminder_time_am_or_pm,reminder_status) VALUES("{}",{},{},"{}","{}")'.format(
        remind_for,
        reminder_time_hours,
        reminder_time_minutes,
        reminder_time_am_or_pm,
        reminder_status
        )
    )

    mydb.commit()
    
