from tkinter import *
from time import strftime
root=Tk()
def time(): 
 string=strftime("%a %I:%M:%S %p")
 b.config(text=string)
 b.after(1000, time)
b=Label(root,font=('courier',80,'bold'),
background='blue',
foreground='white')
b.pack()
time()
root.mainloop()

