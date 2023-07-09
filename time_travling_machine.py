import os
import time
import datetime

def time_travel_to_future():
    time_to_change = ''

    while True:
        time_to_change = datetime.datetime.today() + datetime.timedelta(minutes = 1)

        os.system('sudo timedatectl set-ntp false')
        os.system('sudo date --set="{}"'.format(time_to_change))

        print(time_to_change)

        time.sleep(0.01)


def time_travel_to_present():
    os.system('sudo datetimectl set-ntp true')


time_travel_to_present()


        
    
    
