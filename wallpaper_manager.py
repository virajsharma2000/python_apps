import os
import subprocess
import getpass
import shutil

username = getpass.getuser()

if not os.path.exists('/home/{}/wallpapers'.format(username)):
    os.system('mkdir wallpapers')

if not os.path.exists('/home/{}/wallpapers/wallpaper_trash'.format(username)):
    os.system('mkdir /home/{}/wallpapers/wallpaper_trash'.format(username))

def set_wallpaper(wallpaper_name):
 if os.path.isfile('/home/{}/wallpapers/{}'.format(username,wallpaper_name)):
  if '.' in wallpaper_name:
   if wallpaper_name.split('.')[1] == 'jpg' or wallpaper_name.split('.')[1] == 'jpeg' or wallpaper_name.split('.')[1] == 'png' or wallpaper_name.split('.')[1] == 'gif':
    os.system('gsettings set org.gnome.desktop.background picture-uri file:///home/{}/wallpapers/{}'.format(username,wallpaper_name))

   else:
    print('the wallpaper is not image file')

 else:
  print('the wallpaper does not exist')

def get_current_wallpaper():
    wallpaper_path = subprocess.check_output('gsettings get org.gnome.desktop.background picture-uri'.split()).decode().split('://')[1].replace('\n','',1).replace("'",'',1)
    wallpaper_name = wallpaper_path.split('/')[4]

    return wallpaper_name

def get_wallpapers_stored():
    wallpaper_files = ''
    
    for wallpapers in os.listdir(path = '/home/{}/wallpapers'.format(username)):
        if os.path.isfile('/home/{}/wallpapers/{}'.format(username,wallpapers)):
         if '.' in wallpapers:
          if wallpapers.split('.')[1] == 'jpg' or wallpapers.split('.')[1] == 'jpeg' or wallpapers.split('.')[1] == 'png' or wallpapers.split('.')[1] == 'gif':
            wallpaper_files += wallpapers + '\n'
              
    if any(wallpaper_files):
        return wallpaper_files

    else:
        return 'no wallpapers came yet' 

def delete_wallpaper(wallpaper_name):
 if os.path.isfile('/home/{}/wallpapers/{}'.format(username,wallpaper_name)):
  if '.' in wallpaper_name:
    if wallpaper_name.split('.')[1] == 'jpg' or wallpaper_name.split('.')[1] == 'jpeg' or wallpaper_name.split('.')[1] == 'png' or wallpaper_name.split('.')[1] == 'gif':
     shutil.move('/home/{}/wallpapers/{}'.format(username,wallpaper_name),'/home/{}/wallpapers/wallpaper_trash'.format(username))

  else:
      print('the wallpaper is not image file')

 else:
     print('the wallpaper does not exist')

def restore_wallpaper(wallpaper_name):
    if os.path.isfile('/home/{}/wallpapers/wallpaper_trash/{}'.format(username,wallpaper_name)):
     if '.' in wallpaper_name:
      if wallpaper_name.split('.')[1] == 'jpg' or wallpaper_name.split('.')[1] == 'jpeg' or wallpaper_name.split('.')[1] == 'png' or wallpaper_name.split('.')[1] == 'gif':
       shutil.move('/home/{}/wallpapers/wallpaper_trash/{}'.format(username,wallpaper_name),'/home/{}/wallpapers'.format(username,))

     else:
      print('\n')
      print('the file is not image file')

    else:
     print('\n')
     print('the file does not exist in trash')

def delete_wallpaper_permanently(wallpaper_name):
    if os.path.isfile('/home/{}/wallpapers/wallpaper_trash/{}'.format(username,wallpaper_name)):
     if '.' in wallpaper_name:
      if wallpaper_name.split('.')[1] == 'jpg' or wallpaper_name.split('.')[1] == 'jpeg' or wallpaper_name.split('.')[1] == 'png' or wallpaper_name.split('.')[1] == 'gif':
       os.remove('/home/{}/wallpapers/wallpaper_trash/{}'.format(username,wallpaper_name))

     else:
      print('the file is not image file')

    else:
     print('the file does not exist in trash')

def get_wallpapers_in_trash():
     wallpaper_files = ''
    
     for wallpapers in os.listdir(path = '/home/{}/wallpapers/wallpaper_trash'.format(username)):
        if os.path.isfile('/home/{}/wallpapers/wallpaper_trash/{}'.format(username,wallpapers)):
         if '.' in wallpapers:
          if wallpapers.split('.')[1] == 'jpg' or wallpapers.split('.')[1] == 'jpeg' or wallpapers.split('.')[1] == 'png' or wallpapers.split('.')[1] == 'gif':
            wallpaper_files += wallpapers + '\n'

     if any(wallpaper_files):
      return wallpaper_files

     else:
      return 'wallpaper trash is empty' 

def empty_trash():
    for wallpapers in os.listdir(path = '/home/{}/wallpapers/wallpaper_trash'.format(username)):
        if os.path.isfile('/home/{}/wallpapers/wallpaper_trash/{}'.format(username,wallpapers)):
         if '.' in wallpapers:
          if wallpapers.split('.')[1] == 'jpg' or wallpapers.split('.')[1] == 'jpeg' or wallpapers.split('.')[1] == 'png' or wallpapers.split('.')[1] == 'gif':
            os.remove('/home/{}/wallpapers/wallpaper_trash/{}'.format(username,wallpapers))

while True:    
 print('current wallpaper name - ' + get_current_wallpaper())

 print('\n')

 print('wallpapers existing in wallpapers folder' + '\n\n' + get_wallpapers_stored() + '\n\n' + 'wallpapers sent to trash' + '\n\n' + get_wallpapers_in_trash())

 print('\n')
 
 print('1.set wallpaper')
 print('2.delete wallpaper')
 print('3.restore wallpaper')
 print('4.delete wallpaper permanently')
 print('5.empty trash')

 which_function_to_operate = input('from above which function to operate - type a number of function: ')

 if which_function_to_operate == '1':
    wallpaper_name = input('Enter wallpaper name to set: ')

    set_wallpaper(wallpaper_name)

 elif which_function_to_operate == '2':
    wallpaper_name = input('Enter wallpaper name to delete: ')

    delete_wallpaper(wallpaper_name)

 if which_function_to_operate == '3':
    wallpaper_name = input('Enter wallpaper name to restore: ')

    restore_wallpaper(wallpaper_name)

 if which_function_to_operate == '4':
    wallpaper_name = input('Enter wallpaper name to permanently delete: ')
    
    delete_wallpaper_permanently(wallpaper_name)

 if which_function_to_operate == '5':
     empty_trash()

 print('\n')



