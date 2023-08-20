import os
import subprocess

wallpaper_path = subprocess.check_output('gsettings get org.gnome.desktop.background picture-uri'.split()).decode().replace("'","",2)

if 'file://' in wallpaper_path:
    wallpaper_path = wallpaper_path.split('//')[1]

os.remove(wallpaper_path.replace('\n','',1))

