import smtplib

session = smtplib.SMTP('smtp.gmail.com',587)

print('drink list \n')

file = open('drinks.txt','r')
x = file.read()
print(x)

item = input("Enter drink to order: ")
housenumber = input('Enter house number: ')
societyname = input('Enter socity name: ')
houseaddress = str(housenumber) + ' ' + societyname

if item not in x:
 print('we dont have this item')

else:

 itemsandprices = {'pepsi':'200','sprite':'500','maaza':'600','limca':'700'}

 print('price of ' + item + ' is: ' + itemsandprices.get(item))

 orderconform = input('do you want to order ' + item + ': ')

 if orderconform == 'yes':

  session.starttls()
  session.login('your_email','your_email_password')
  session.sendmail('your_email','deliveryguy_email','item is {item} house address is {houseaddress}'.format(item = item,houseaddress = houseaddress))
  session.quit()
  print('ordered successfully!!')

 if orderconform == 'no':
  pass
