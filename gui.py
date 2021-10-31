from tkinter import *
top=Tk()
top.title("button")
top.geometry("200x300")
b=Button(top,text="simple",bg="blue",fg="white",command=top.destroy)
b.pack()
top.mainloop()
