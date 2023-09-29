import psutil
import os

processes = psutil.process_iter()

for procs in processes:
    process_name = procs.name()

    os.system('killall {}'.format(process_name))
