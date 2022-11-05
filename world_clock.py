import datetime
import pytz
import tkinter

r = tkinter.Tk()
r.title('world clock')

def get_time():
    time_zones = {
                 'india':'asia/kolkata',
                 'london':'europe/london',
                 'new_york':'america/new_york',
                 'sydney':'australia/sydney'
                 }

    current_time1 = datetime.datetime.now(pytz.timezone(time_zones.get('india'))).strftime('%d - %B - %A - %Y  %I:%M:%S %P')
    current_time2 = datetime.datetime.now(pytz.timezone(time_zones.get('london'))).strftime('%d - %B - %A - %Y  %I:%M:%S %P')
    current_time3 = datetime.datetime.now(pytz.timezone(time_zones.get('new_york'))).strftime('%d - %B - %A - %Y  %I:%M:%S %P')
    current_time4 = datetime.datetime.now(pytz.timezone(time_zones.get('sydney'))).strftime('%d - %B - %A - %Y  %I:%M:%S %P')
    



    lbl.config(text = 'india \n {} \n\n london \n {} \n\n new_york \n {} \n\n sydney \n {} '.format(current_time1,current_time2,current_time3,current_time4))
    lbl.after(1000,get_time)

    


lbl = tkinter.Label(r,font = 'courier')

get_time()

lbl.pack()

r.mainloop()
