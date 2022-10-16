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

 c.execute('select * from reminders')

 r = c.fetchall()
 for records in r:
   
   if int(time.strftime('%I')) == records[2] and int(time.strftime('%M')) == records[3] and time.strftime('%P') == records[4]:
        status = records[5]
        sound_to_play = records[6]

        if status == 'pending':
         remind_for = records[1]
         plyer.notification.notify(title = 'Reminder',message = remind_for)
         playsound.playsound(sound_to_play)

         c.execute('UPDATE reminder SET reminder_status="completed" WHERE reminder_id={}'.format(record[0]))
         mydb.commit()

        if status == 'completed':
            continue

        if status == 'cancelled':
            continue

        if status == 'repeated':
            remind_for = records[1]
            plyer.notification.notify(title = 'Reminder',message = remind_for)
            playsound.playsound('alarmsiren.mp3')

   else:
      continue

   time.sleep(60)
      

 

  
