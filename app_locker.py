import psutil
import os
import signal

while True:
    apps_not_allowed_lists = ['gedit']

    for proc in psutil.process_iter():
        process_name = proc.name()
        process_id = proc.pid

        if process_name in apps_not_allowed_lists:
            os.kill(process_id,signal.SIGKILL)


            
            
