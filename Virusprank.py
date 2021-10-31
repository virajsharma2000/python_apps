from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("200x300")
def virus():
 import time
 while True:
  messagebox.showerror('Virus','alert Virus is dectected')
  time.sleep(1)
x = Button(root, text = 'check Virus', command = virus)
x.pack()
root.mainloop()
