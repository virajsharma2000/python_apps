import tkinter
import os
import webbrowser
import easygui

tk = tkinter.Tk()

tk.title('welcome to TeaMug')

def save_as(root,html_code):
    
    file_name = easygui.filesavebox()

    root.title(file_name)

    file = open(file_name,'w')
    file.write(html_code.get('1.0','end-1c'))
    file.close()

def save(root,html_code):
    
    file_name = root.title()

    if file_name == 'untitled':
       save_as(root,html_code)

    else:
        file = open(file_name,'w')
        file.write(html_code.get('1.0','end-1c'))
        file.close()

def run_file(root):
    file_name = root.title()

    current_directory = os.getcwd()

    webbrowser.open('file:///' + file_name)

def new_file():
    r = tkinter.Tk()

    r.title('untitled')

    html_code = tkinter.Text(r)

    save_file_button = tkinter.Button(r,text = 'Save',command = lambda: save(r,html_code))
    save_as_file_button = tkinter.Button(r,text = 'Save As',command = lambda: save_as(r,html_code))
    run_file_button = tkinter.Button(r,text = 'Run',command = lambda: run_file(r))

    html_code.grid(row = 1)
    save_file_button.grid(row = 2)
    save_as_file_button.grid(row = 3)
    run_file_button.grid(row = 4)

    r.mainloop()


def open_existing_file():
     file_name = easygui.fileopenbox()
     
     r = tkinter.Tk()

     r.title(file_name)

     file_text = open(r.title(),'r').read()
     
     html_code = tkinter.Text(r)

     html_code.insert(tkinter.END,file_text)

     save_file_button = tkinter.Button(r,text = 'Save',command = lambda: save(r,html_code))
     save_as_file_button = tkinter.Button(r,text = 'Save As',command = lambda: save_as(r,html_code))
     run_file_button = tkinter.Button(r,text = 'Run',command = lambda: run_file(r))

     html_code.grid(row = 1)
     save_file_button.grid(row = 2)
     save_as_file_button.grid(row = 3)
     run_file_button.grid(row = 4)

     r.mainloop()

    
open_file_button = tkinter.Button(tk,text = 'open existing file',command = open_existing_file)
new_file_button = tkinter.Button(tk,text = 'create new file',command = new_file)

open_file_button.pack(side = 'left')
new_file_button.pack(side = 'left')

tk.mainloop()

    
    
