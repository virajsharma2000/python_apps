import turtle

def render(file_name):
 pen = turtle.Pen()

 if '.' in file_name:
  if file_name.split('.')[1] == 'dml':
   for line in open(file_name,'r').read().split('\n'):
      
    if line.startswith('<forward>') and line.endswith('</forward>'):
     pen.forward(int(line.split('>')[1].split('</')[0]))

    if line.startswith('<backward>') and line.endswith('</backward>'):
     pen.backward(int(line.split('>')[1].split('</')[0]))

    if line.startswith('<left>') and line.endswith('</left>'):
     pen.left(int(line.split('>')[1].split('</')[0]))

    if line.startswith('<right>') and line.endswith('</right>'):
     pen.right(int(line.split('>')[1].split('</')[0]))


file_name = input('Enter file name: ')

render(file_name)
    
   
 
