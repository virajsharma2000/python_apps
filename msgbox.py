from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("200x300")
def msg():
 messagebox.showerror('haww!','haww! you have done something wrong')
 messagebox.showwarning('warning for wrong ','when you will do wrong with this city your computer will be damaged')
x = Button(root, text = 'msg', command = msg)
x.pack()
root.mainloop()
