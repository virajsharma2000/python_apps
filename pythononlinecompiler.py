import easygui

x = input("do you want to run compiler or create file or edit file: ")

if x == 'run compiler':
 file = easygui.fileopenbox('python compiler')
 exec(open(file,'r').read())

if x == 'create file':
    code = easygui.textbox('python file creator')
    filename = easygui.filesavebox('python file creator')

    file = open(filename,'w')
    file.write(code)
    file.close()

if x == 'edit file':
    filename = easygui.fileopenbox('python file editor')
    code = easygui.textbox('','python file editor',open(filename,'r').read())
    
    file = open(filename,'w')
    file.write(code)
    file.close()
