from tkinter import *
from tkinter import messagebox
import easygui
from PIL import Image
import os

filepath = 'Untitled'

root = Tk()

root.title('Easy Painting - {}'.format(filepath))

canvas = Canvas(root,width = root.winfo_screenwidth(),height = root.winfo_screenheight() - 200,highlightbackground = 'Black')

class Brush:
 def __init__(self,brush_color,brush_size,erase_mode):
  self.brush_color = brush_color
  self.brush_size = brush_size
  self.erase_mode = erase_mode

 def paint(self,event):
  global canvas
  global filepath

  if not self.erase_mode:
   canvas.create_oval(event.x,event.y,event.x + self.brush_size,event.y + self.brush_size,outline = self.brush_color,fill = self.brush_color)

   if not filepath.endswith('*'):
    filepath += '*'
    root.title('Easy Painting - {}'.format(filepath))
   
  else:
   canvas.create_oval(event.x,event.y,event.x + self.brush_size,event.y + self.brush_size,outline = canvas['background'],fill = canvas['background'])

   if not filepath.endswith('*'):
    filepath += '*'
    root.title('Easy Painting - {}'.format(filepath))
   

brush_color = 'Black'
brush_size = 1
erase_mode = False

def change_brush_color():
 global brush_color
  
 brush_color = easygui.buttonbox('change color of brush','Easy Painting',['Black','Red','Green','Blue','Purple','Yellow','Pink','Cyan','Magenta'])

 canvas.bind('<B1-Motion>',Brush(brush_color,brush_size,erase_mode).paint)
 canvas.bind('<Button>',Brush(brush_color,brush_size,erase_mode).paint)

def change_brush_size():
 global brush_size

 brush_size = int(easygui.buttonbox('change brush size','Easy Painting',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']))
 
 canvas.bind('<B1-Motion>',Brush(brush_color,brush_size,erase_mode).paint)
 canvas.bind('<Button>',Brush(brush_color,brush_size,erase_mode).paint)

def turn_on_eraser_mode():
 global erase_mode
 
 erase_mode = True

 canvas.bind('<B1-Motion>',Brush(brush_color,brush_size,erase_mode).paint)
 canvas.bind('<Button>',Brush(brush_color,brush_size,erase_mode).paint)

def turn_off_eraser_mode():
 global erase_mode

 erase_mode = False

 canvas.bind('<B1-Motion>',Brush(brush_color,brush_size,erase_mode).paint)
 canvas.bind('<Button>',Brush(brush_color,brush_size,erase_mode).paint)

def clear_painting():
 canvas.delete('all')


def save_file():
 global filepath

 if filepath == 'Untitled' or filepath == 'Untitled*':
  filepath = easygui.filesavebox()

  extension = os.path.basename(filename).split('.')[1]

  if extension == 'ps':
   canvas.postscript(file = filepath,colormode = 'color')

   root.title('Easy Painting - {}'.format(filepath))

  else:
   messagebox.showerror('Easy Painting','The file is not a postscript file')
   
 else:
  filepath = filepath.replace('*','')
  
  canvas.postscript(file = filepath,colormode = 'color')

  root.title('Easy Painting - {}'.format(filepath))

def share_file():
 filename = easygui.fileopenbox()

 extension = os.path.basename(filename).split('.')[1]

 if extension == 'ps' or extension == 'png':
  webbrowser.open('web.whatsapp.com/send?attachment=' + filename)

 else:
  messagebox.showerror('Easy Painting','The file is not a postscript file or a image file')
  
def postscript_to_png():
 filename = easygui.fileopenbox()

 extension = os.path.basename(filename).split('.')[1]

 if extension == 'ps':
  image = Image.open(filename)

  os.remove(filename)
  
  image.save(filename.replace('.ps','.png'))

 else:
  messagebox.showerror('Easy Painting','The file is not a postscript file')

def png_to_postscript():
 filename = easygui.fileopenbox()

 extension = os.path.basename(filename).split('.')[1]

 if extension == 'png':
  image = Image.open(filename)

  os.remove(filename)
  
  image.save(filename.replace('.png','.ps'))

 else:
  messagebox.showerror('Easy Painting','The file is not a image file')
 

def paint_menu():
 tk = Tk()

 change_color_button = Button(tk,text = 'Change Brush Color',command = lambda: change_brush_color())
 change_size_button = Button(tk,text = 'Change Brush Size',command = lambda: change_brush_size())
 turn_on_eraser_mode_button = Button(tk,text = 'Turn On Eraser Mode',command = lambda: turn_on_eraser_mode())
 turn_off_eraser_mode_button = Button(tk,text = 'Turn Off Eraser Mode',command = lambda: turn_off_eraser_mode())
 clear_canvas_button = Button(tk,text = 'Clear Painting',command = lambda: clear_painting())

 change_color_button.grid(row = 1)
 change_size_button.grid(row = 2)
 turn_on_eraser_mode_button.grid(row = 3)
 turn_off_eraser_mode_button.grid(row = 4)
 clear_canvas_button.grid(row = 5)

 tk.mainloop()

def file_menu():
 tkinter_object = Tk()

 file_save_button = Button(tkinter_object,text = 'Save File',command = lambda: save_file())
 share_file_button = Button(tkinter_object,text = 'Share File in web whatsapp',command = lambda: share_file())
 postscript_to_png_button = Button(tkinter_object,text = 'Convert your postscript file to image file',command = lambda: postscript_to_png())
 png_to_postscript_button = Button(tkinter_object,text = 'Convert your image file to postscript file',command = lambda: png_to_postscript())

 file_save_button.grid(row = 1)
 share_file_button.grid(row = 2)
 postscript_to_png_button.grid(row = 3)
 png_to_postscript_button.grid(row = 4)

 tkinter_object.mainloop()
  

canvas.bind('<B1-Motion>',Brush(brush_color,brush_size,erase_mode).paint)
canvas.bind('<Button>',Brush(brush_color,brush_size,erase_mode).paint)

paint_menu_button = Button(text = 'Paint Menu',command = lambda: paint_menu())
file_menu_button = Button(text = 'File Menu',command = lambda: file_menu())

canvas.grid(row = 1)

paint_menu_button.grid(row = 2)
file_menu_button.grid(row = 3)

root.mainloop()


