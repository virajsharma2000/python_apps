import tkinter
import easygui
r = tkinter.Tk()
r.title('normal text editor')
def savefile():
 x = inptxt.get('1.0','end-1c')
 saveinit = open(easygui.filesavebox(),'w')
 saveinit.write(x)
 saveinit.close()
def openfile():
 p = open(easygui.fileopenbox(),'r')
 x = p.read()
 o = tkinter.Label(r,text = x)
 o.pack()
inptxt = tkinter.Text(r)
b = tkinter.Button(r,text = 'save',command = savefile)
p = tkinter.Button(r,text = 'open',command = openfile)
inptxt.pack()
b.pack()
p.pack()
r.mainloop()
