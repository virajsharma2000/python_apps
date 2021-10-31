from tkinter import *
top=Tk()
top.geometry("200x300")
import datetime
x=datetime.datetime.now()
print(x)
b=Label(top,text=str(x),bg="lightblue",fg="white")
b.pack()
top.mainloop()
