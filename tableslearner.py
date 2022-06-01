import webbrowser

scores = 0

a = int(input('2 x 1: '))

if 2 * 1 == a:
 scores += 1
else:
 scores += 0

b = int(input('2 x 2: '))

if 2 * 2 == b:
 scores += 1
else:
 scores += 0

c = int(input('2 x 3: '))

if 2 * 3 == c:
 scores += 1
else:
 scores += 1

d = int(input('2 x 4: '))

if 2 * 4 == d:
 scores += 1
else:
 scores += 0

c = int(input('2 x 5: '))

if 2 * 5 == c:
 scores += 1
else:
 scores += 0

d = int(input('2 x 6: '))

if 2 * 6 == d:
 scores += 1
else:
 scores += 0

e = int(input('2 x 7: '))

if 2 * 7 == e:
 scores += 1
else:
 scores += 0

f = int(input('2 x 8: '))

if 2 * 8 == f:
 scores += 1
else:
 scores += 0

g = int(input('2 x 9: '))

if 2 * 9 == g:
 scores += 1
else:
 scores += 0

h = int(input('2 x 10: '))

if 2 * 10 == h:
 scores += 1
else:
 scores += 0


print('your scores are:',scores)

share = input('do you want to share your scores to your friends: ')

if share == 'yes':
 webbrowser.open('https://web.whatsapp.com/send?text=' + 'I won in a app called tables learner my scores are ' + str(scores) + ' if you want to get scores like this then install tableslearner and show my your scores like this')

if share == 'no':
 pass

