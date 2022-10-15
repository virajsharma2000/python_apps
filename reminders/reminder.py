import time
import mysql.connector
import plyer
import playsound

mydb = mysql.connector.connect(
host = 'localhost',
username = 'viraj',
password = 'pumpulili',
database = 'viraj'
)

while True:


 c = mydb.cursor()

 c.execute('select reminder_id, reminder_status, remind_for,  reminder_time_hours, reminder_time_minutes, reminder_time_am_or_pm from reminders')

 r = c.fetchall()
 for records in r:
   
   if int(time.strftime('%I')) == records[3] and int(time.strftime('%M')) == records[4] and time.strftime('%P') == records[5]:
        status = record[1]

        if status == 'pending':
         remind_for = records[2]
         plyer.notification.notify(title = 'Reminder',message = remind_for)
         playsound.playsound('alarmsiren.mp3')

         c.execute('UPDATE reminder SET reminder_status="completed" WHERE reminder_id={}'.format(record[0]))
         mydb.commit()

        if status == 'completed':
            continue

        if status == 'cancelled':
            continue

        if status == 'repeated':
            remind_for = records[2]
            plyer.notification.notify(title = 'Reminder',message = remind_for)
            playsound.playsound('alarmsiren.mp3')

   else:
      continue

 time.sleep(60)
      

 

  
