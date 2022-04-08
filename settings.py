import os
import subprocess
import psutil
import shutil

print("welcome to linux wifi and battery settings")

def connecttowifi():
 wifies = subprocess.check_output(['nmcli','device','wifi','list']).decode('utf-8')
 l = wifies.split('\n')
 for x in l[1:]:
     print(x[26:49],str('\n'))
 wifi = input("type here any wifi name after seeing from above wifi list: ")
 os.system('nmcli con up "' + wifi + '"')

def airplainmode():
 x = input("turn on wifi or turn off wifi: ")
 if x == 'turn off wifi':
  os.system('nmcli r wifi off')
 if x == 'turn on wifi':
  os.system('nmcli r wifi on')
  
def wifi():
 print('wifi settings')
 x = input("wifi connection or air plain mode: ")
 if x == 'wifi connection':
  connecttowifi()
 if x == 'air plain mode':
  airplainmode()



def check_battery_percent():
 init = psutil.sensors_battery()
 x = int(init.percent) 
 print(x)
 
def battery():
 print("battery settings")
 x = input("the battery settings just has check battery percent then do you want to check the battery percentage: ")
 if x == 'check battery percent':
  check_battery_percent()


x = input("wifi settings or battery settings: ")
if x == 'wifi settings':
 wifi()
if x == 'battery settings':
 battery()
