import os
x = input("Enter command of yes or no to shutdown your computer y n: ")
if x == "y":
 os.system('shutdown/s /t 1')
if x == "n":
 exit()
if x == "":
    print("no no no! write a command")
    
