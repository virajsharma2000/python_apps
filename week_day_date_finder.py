import datetime

week_day = input('Enter weekday that you want to find date: ')


days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
months = ['','January','February','March','April','May','June','July','August','September','October','November','December']

how_much_days_after_weekday = days.index(week_day.capitalize()) - days.index(datetime.datetime.now().strftime('%A'))


week_day_date = datetime.date.today() + datetime.timedelta(days = how_much_days_after_weekday)

date = str(months[week_day_date.month]) + ' ' + str(week_day_date.day) + ',' + str(week_day_date.year)

print(date)
