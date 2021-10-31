from tkinter import *
from time import strftime
r = Tk()
def time():
 string = strftime("%I:%M:%S")
 lbl.config(text = string)
 lbl.after(1000, time)
lbl = Label(r,font = ('courier',80,'bold'),background = 'blue',foreground = 'white')
lbl.pack()
time()
r.mainloop()
