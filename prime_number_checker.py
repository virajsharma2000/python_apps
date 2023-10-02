def check_prime_number(number):
 divisible_by_two = number % 2 == 0
 divisible_by_three = number % 3 == 0
 divisible_by_four = number % 4 == 0
 divisible_by_five = number % 5 == 0
 divisible_by_six = number % 6 == 0
 divisible_by_seven = number % 7 == 0
 divisible_by_eight = number % 8 == 0
 divisible_by_nine = number % 9 == 0

 if number == 2:
     if divisible_by_three or divisible_by_four or divisible_by_five or divisible_by_six or divisible_by_seven or divisible_by_eight or divisible_by_nine:
         return False

     else:
         return True

 elif number == 3:
     if divisible_by_two or divisible_by_four or divisible_by_five or divisible_by_six or divisible_by_seven or divisible_by_eight or divisible_by_nine:
         return False
        
     else:
         return True

 elif number == 4:
       if divisible_by_two or divisible_by_three or divisible_by_five or divisible_by_six or divisible_by_seven or divisible_by_eight or divisible_by_nine:
         return False

       else:
         return True

 elif number == 5:
     if divisible_by_two or divisible_by_three or divisible_by_four or divisible_by_six or divisible_by_seven or divisible_by_eight or divisible_by_nine:
         return False

     else:
         return True

 elif number == 6:
     if divisible_by_two or divisible_by_three or divisible_by_four or divisible_by_five or divisible_by_seven or divisible_by_eight or divisible_by_nine:
         return False

     else:
         return True

 elif number == 7:
     if divisible_by_two or divisible_by_three or divisible_by_four or divisible_by_five or divisible_by_six or divisible_by_eight or divisible_by_nine:
         return False

     else:
         return True

 elif number == 8:
     if divisible_by_two or divisible_by_three or divisible_by_four or divisible_by_five or divisible_by_six or divisible_by_seven or divisible_by_nine:
         return False

     else:
         return True

 elif number == 9:
      if divisible_by_two or divisible_by_three or divisible_by_four or divisible_by_five or divisible_by_six or divisible_by_seven:
         return False

      else:
         return True

 else:
     if divisible_by_two or divisible_by_three or divisible_by_four or divisible_by_five or divisible_by_six or divisible_by_seven or divisible_by_eight or divisible_by_nine:
         return False

     else:
         return True

def divisible_by(number):
    divisible_by_numbers = ''
    i = 1
    
    while i != 9:
        i += 1
        
        if number % i == 0:
         if i != number:
            divisible_by_numbers += '\n' + str(i)

    return divisible_by_numbers

     
while True:
 number = int(input('Enter number: '))

 if check_prime_number(number):
    print('Prime')

 else:
    print('Composite')
    print('divisible by {}'.format(divisible_by(number)))
      
     
