import time
import psutil

print('MACROLINUS OS')
print('CREATED BY -> "THE BEST PYTHON PROGRAMMER"')

print('\n')

currentdate = time.strftime('%B,%A %Y')
print(currentdate)

def macrolinus():
 while True:
    print('1 app.calculator')
    print('2 app.python3')
    print('3 app.timer')
    print('4 app.about os')
    print('5 app.battery')
    
    print('\n')
    
    app = input('Enter app: ')
    
    if app == 'calculator':
        
        number1 = int(input('Enter first number: '))
        number2 = int(input("Enter second number: "))
        operator = input('Enter sign: ')
        
        if operator == '/':
         if number1 == 0 or number2 == 0:
             print('zeros cannot be divided')
             
         else:
            print(int(number1 / number2))

         print('\n')
            
        if operator == '*':
            print(number1 * number2)

        print('\n')
            
        if operator == '+':
            print(number1 + number2)

        print('\n')
            
        if operator == '-':
            print(number1 - number2)


        print('\n')
            
    if app == 'python3':
     lines = int(input("Enter how much lines of code you want to write: "))

     for line in range(lines):
         try:
            programme = input("type here: ")
            exec(programme)
            
         except:
             print('some Error occured')
             continue

     print('\n')
         
    if app == 'timer':
        minutes = int(input('Enter minutes: '))
        
        time.sleep(minutes * 60)
        
        print('time is up')


        print('\n')

    if app == 'about os':
        print('this is os called macrolinus created by "viraj sharma"')
        print('with 4 apps')
        print('this os is created using python language')
        print('it ends app automatically')
        print('when you see a litttle bit enter that means the app has ended')
        print('\n')

    if app == 'battery':
        print(int(psutil.sensors_battery().percent),'%')

        print('\n')
        


password = input('Enter your password: ')

if password == 'pumpulili' or password == 'putchi':
    macrolinus()
    
else:
    print('wrong password')
