# importing important libarys

import tkinter
import easygui

# creating window titled - "untitled"

r = tkinter.Tk()
r.title('untitled')


# creating functions

# creating function called saveasfile

def saveasfile():
    # taking text varible
    
    global text

    # making file saving box
    
    filename = easygui.filesavebox()

    # saving as the file

    file = open(filename,'w')
    file.write(text.get('1.0','end-1c'))
    file.close()

    # replacing the tkinter title

    r.title(filename)


# creating function called savefile


def savefile():

     # taking text varible
    
    global text

    # checking if the file is untitled
    # if file is untitled then
    # else editing the file
    
    if r.title() == 'untitled':
        saveasfile()

    else:
        file = open(r.title(),'w')
        file.write(text.get('1.0','end-1c'))
        file.close()

# creating function called openfile

def openfile():
    # taking varible called text
    
    global text

    # making fileopenbox

    filename = easygui.fileopenbox()

    # deleteing orignial text

    text.delete('1.0','end-1c')

    # reading the file and inserting the text of file

    text.insert('1.0',open(filename,'r').read())

    # replacing the title

    r.title(filename)

# creating function called newfile

def newfile():
    # taking the varible called  text
    
    global text

    # deleteing the original text

    text.delete('1.0','end-1c')

    #  renaming the title to untitled file

    r.title('untitled')

# making all editing  text written in textarea function

# creating function called cut_text

def cut_text():
    # taking the varible called text
    
    global text

    # generating the event to cut thing from text area


    text.event_generate('<<Cut>>')

def copy_text():
    # taking the variable called text

    global text

     # generating the event to cut thing from text area


    text.event_generate('<<Copy>>')

def paste_text():
    # taking the varible called text
    
    global text

    # generating the event to paste thing from text area


    text.event_generate('<<Paste>>')



def select_all_text():
    # taking the varible text
    
    global text
    
     # generating the event to salecting all things from text area

    text.event_generate('<<SelectAll>>')

def delete_all_text():
    global text

    text.delete('1.0','end-1c')

# creating function called python

def python():
    # taking varible called text
    
    global text

    # executing the python code from varible called text

    exec(text.get('1.0','end-1c'))



# creating text area with varible  named text

text = tkinter.Text(r)

# creating all buttons for file

saveasfile_button = tkinter.Button(r,text = 'Save As',command = saveasfile)
savefile_button = tkinter.Button(r,text = 'Save',command = savefile)
openfile_button = tkinter.Button(r,text = 'Open',command = openfile)
newfile_button = tkinter.Button(r,text = 'New',command = newfile)

# creating the buttons for editing text written in text area

cut_text_button = tkinter.Button(r,text = 'Cut',command = cut_text)
copy_text_button = tkinter.Button(r,text = 'Copy',command = copy_text)
paste_text_button = tkinter.Button(r,text = 'Paste',command = paste_text)
select_all_text_button = tkinter.Button(r,text = 'Select All',command = select_all_text)
delete_all_text_button = tkinter.Button(r,text = 'Delete all',command = delete_all_text)



# packing text area in tkinter window

text.pack()

# packing all buttons of file in tkinter window

saveasfile_button.pack()
savefile_button.pack()
openfile_button.pack()
newfile_button.pack()

# packing all buttons of editing text written in text area 

cut_text_button.pack()
copy_text_button.pack()
paste_text_button.pack()
select_all_text_button.pack()
delete_all_text_button.pack()




# ending the tkinter

r.mainloop()
    
