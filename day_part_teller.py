import time

print('current time:{} {}'.format(time.strftime('%I'),time.strftime('%P')))

print()

def current_day_part(hours,am_or_pm):
 day = ''

 if hours <= 12:
  if am_or_pm == 'pm':
   if int(hours) >= 7:
     day = 'Night'

   if int(hours) == 12 or int(hours) >= 1 and not int(hours) >= 4:
     day = 'Afternoon'

   if int(hours) >= 4 and not int(hours) >= 12 and not int(hours) >= 7:
     day = 'Evening'

  

  if am_or_pm == 'am':
    if int(hours) >= 4 and not int(hours) >= 12:
     day = 'Morning'

    if int(hours) == 12 or int(hours) >= 1 and not int(hours) >= 4:
     day = 'Night'

  return day

hours = int(input('current hours: '))
am_or_pm = input('am / pm: ')

print(current_day_part(hours,am_or_pm))
