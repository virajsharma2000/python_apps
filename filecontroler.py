from tkinter import *
import os
import easygui
import shutil
from tkinter import filedialog
from tkinter import messagebox as mb
r = Tk()
def window_open():
 read = easygui.fileopenbox()
 return read
def copy_file():
 x = window_open()
 y = filedialog.askdirectory()
 shutil.copy(x, y)
 mb.showinfo('conformation','file copied!')
def move_file():
 x = window_open()
 y = filedialog.askdirectory()
 shutil.move(x, y)
 mb.showinfo('conformation','file moved!')
def remove_file():
 x = window_open()
 os.remove(x)
 mb.showinfo('conformation','file removed!')
Button(r, text = 'copy file',command = copy_file).grid(row = 21, column = 2)
Button(r, text = 'move file',command = move_file).grid(row = 22, column = 2)
Button(r, text = 'remove file',command  = remove_file).grid(row = 23, column = 2)
r.mainloop()
 
 
