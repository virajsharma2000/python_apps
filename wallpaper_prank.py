import os
import glob
import getpass
import random
import time

for i in range(10):
    images = glob.glob('*.jpg') + glob.glob('*.jpeg') + glob.glob('*.png')

    random.shuffle(images)

    username = getpass.getuser()
    
    for wallpapers in images:
        os.system('gsettings set org.gnome.desktop.background picture-uri file:///home/{}/{}'.format(username,wallpapers))
        time.sleep(1)   

