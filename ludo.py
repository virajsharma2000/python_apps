import random

player1_goti1 = 0
player1_goti2 = 0
player1_goti3 = 0
player1_goti4 = 0

player2_goti1 = 0
player2_goti2 = 0
player2_goti3 = 0
player2_goti4 = 0

player_turn = 0

def roll():
 min_number = 1
 max_number = 6

 roll = random.randint(min_number,max_number)

 return roll

def run_goti(number,goti_number,player_number):
  global player1_goti1
  global player1_goti2
  global player1_goti3
  global player1_goti4
  
  global player2_goti1
  global player2_goti2
  global player2_goti3
  global player2_goti4
 
  if player_number == 1:
   if goti_number == 1:
    player1_goti1 += number

   if goti_number == 2:
    player1_goti2 += number

   if goti_number == 3:
    player1_goti3 += number

   if goti_number == 4:
    player1_goti4 += number

  if player_number == 2:
   if goti_number == 1:
    player2_goti1 += number

   if goti_number == 2:
    player2_goti2 += number

   if goti_number == 3:
    player2_goti3 += number

   if goti_number == 4:
    player2_goti4 += number

def wake_up_goti(goti_number,player_number):
 global player1_goti1
 global player1_goti2
 global player1_goti3
 global player1_goti4
  
 global player2_goti1
 global player2_goti2
 global player2_goti3
 global player2_goti4
 
 if player_number == 1:
  if goti_number == 1:
   player1_goti1 = 1

  if goti_number == 2:
   player1_goti2 = 1

  if goti_number == 3:
   player1_goti3 = 1

  if goti_number == 4:
   player1_goti4 = 1

 if player_number == 2:
  if goti_number == 1:
   player2_goti1 = 1

  if goti_number == 2:
   player2_goti2 = 1

  if goti_number == 3:
   player2_goti3 = 1

  if goti_number == 4:
   player2_goti4 = 1


for i in range(20):
 player_turn += 1

 print("Player {}'s turn".format(player_turn))

 if player_turn == 1:
  print('Player1 goties =', player1_goti1, player1_goti2, player1_goti3, player1_goti4)

  print('Player2 goties =' , player2_goti1,player2_goti2,player2_goti3, player2_goti4)

  input('Press Enter to roll: ')

  value = roll()

  print('You got',value)
  
  goti_number = int(input('Enter goti number: '))
  
  player1_goties = {'1':player1_goti1,'2':player1_goti2,'3':player1_goti3,'4':player1_goti4}

  if value == 1 or value == 6:
   if int(player1_goties.get(str(goti_number))) == 0:
    wake_up_goti(goti_number,player_turn)

   else:
    run_goti(1,goti_number,player_turn)

  else:
   if int(player1_goties.get(str(goti_number))) != 0:
    run_goti(value,goti_number,player_turn)

  if value == 6:
   player_turn = 0

 if player_turn == 2:
  print('Player1 goties =', player1_goti1, player1_goti2, player1_goti3, player1_goti4)

  print('Player2 goties =' , player2_goti1,player2_goti2,player2_goti3, player2_goti4)

  input('Press Enter to roll: ')

  value = roll()

  print('You got',value)
  
  goti_number = int(input('Enter goti number: '))
  
  player2_goties = {'1':player2_goti1,'2':player2_goti2,'3':player2_goti3,'4':player2_goti4}

  if value == 1 or value == 6:
   if int(player2_goties.get(str(goti_number))) == 0:
    wake_up_goti(goti_number,player_turn)

   else:
    run_goti(1,goti_number,player_turn)

  else:
   if int(player2_goties.get(str(goti_number))) != 0:
    run_goti(value,goti_number,player_turn)

  if value == 6:
   player_turn = 1

  else:
   player_turn = 0
 

player1_total_score = player1_goti1 + player1_goti2 + player1_goti3 + player1_goti4
player2_total_score = player2_goti1 + player2_goti2 + player2_goti3 + player2_goti4

if player1_total_score > player2_total_score:
 print('Player1 wins!!')

if player1_total_score < player2_total_score:
 print('Player2 wins!!')
 
if player1_total_score == player2_total_score:
 print('Tie!!')
