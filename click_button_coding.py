import tkinter
import easygui

r = tkinter.Tk()

program = ''

def times():
    global program
    
    number = easygui.enterbox('Enter how many times this program should execute')

    program += 'for x in range({}):\n\t'.format(number)


def next_line():
    global program
    
    program += '\n'


def for_loop():
    global program
    
    new_variable_name = easygui.enterbox('Enter new for loop variable name')
    array_varible_name = easygui.enterbox('Enter array varible name')
    
    program += 'for {} in {}:\n '.format(new_variable_name,array_varible_name)


def create_array():
    global program
    
    things_in_array = easygui.enterbox('Enter things in the array')

    program += '{}'.format(things_in_array.split())
    

def create_variable():
    global program
    
    varible_name = easygui.enterbox('Enter new variable name')

    program += '{} = '.format(varible_name)

   
def print_variable():
    global program
    
    varible_name = easygui.enterbox('Enter variable name to print')

    program += 'print({})'.format(varible_name)

    
def create_string():
    global program
    
    text = easygui.enterbox('Enter string text')

    program += '"{}"'.format(text)

    
    

def run_program():
    global program
    
    exec(program)
    


tkinter.Button(r,text = 'times',command = times).pack(side = 'left')
tkinter.Button(r,text = 'next line',command = next_line).pack(side = 'left')
tkinter.Button(r,text = 'for loop',command = for_loop).pack(side = 'left')

tkinter.Button(r,text = 'create array',command = create_array).pack(side = 'left')
tkinter.Button(r,text = 'create variable',command = create_variable).pack(side = 'left')
tkinter.Button(r,text = 'print variable',command = print_variable).pack(side = 'left')

tkinter.Button(r,text = 'create string',command = create_string).pack(side = 'left')
tkinter.Button(r,text = 'Run',command = run_program).pack(side = 'left')

r.mainloop()


    
    
