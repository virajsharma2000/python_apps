# neccessary dependencies
from decimal import Decimal

# for patenting my name 
print("Thanks for using mathematics module created by viraj sharma to view source code goto https://github.com/virajsharma2000/python_apps/blob/main/mathematics.py")

# dictnoary of number names for time to text
number_names = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
    16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
    21: "twenty-one", 22: "twenty-two", 23: "twenty-three", 24: "twenty-four", 25: "twenty-five",
    26: "twenty-six", 27: "twenty-seven", 28: "twenty-eight", 29: "twenty-nine", 30: "thirty",
    31: "thirty-one", 32: "thirty-two", 33: "thirty-three", 34: "thirty-four", 35: "thirty-five",
    36: "thirty-six", 37: "thirty-seven", 38: "thirty-eight", 39: "thirty-nine", 40: "forty",
    41: "forty-one", 42: "forty-two", 43: "forty-three", 44: "forty-four", 45: "forty-five",
    46: "forty-six", 47: "forty-seven", 48: "forty-eight", 49: "forty-nine", 50: "fifty",
    51: "fifty-one", 52: "fifty-two", 53: "fifty-three", 54: "fifty-four", 55: "fifty-five",
    56: "fifty-six", 57: "fifty-seven", 58: "fifty-eight", 59: "fifty-nine", 60: "sixty"
}

# intresting mathematicians
mathematicians = {
    "Isaac Newton": {
        "Description": "English mathematician who co-invented calculus and made significant contributions to classical mechanics and optics.",
        "BirthDate": "1643-01-04",
        "DeathDate": "1727-03-31",
        "KeyWorks": ["Calculus", "Laws of Motion", "Universal Gravitation"]
    },
    "Leonhard Euler": {
        "Description": "Swiss mathematician known for his work in graph theory, topology, and introducing the modern notation for functions and constants like 'e'.",
        "BirthDate": "1707-04-15",
        "DeathDate": "1783-09-18",
        "KeyWorks": ["Euler's Formula", "Graph Theory", "Number Theory"]
    },
    "Carl Friedrich Gauss": {
        "Description": "German mathematician who contributed to number theory, geometry, statistics, and the theory of magnetism.",
        "BirthDate": "1777-04-30",
        "DeathDate": "1855-02-23",
        "KeyWorks": ["Gaussian Elimination", "Prime Number Theorem", "Electromagnetic Theory"]
    },
    "Euclid": {
        "Description": "Ancient Greek mathematician often referred to as the 'Father of Geometry'.",
        "BirthDate": "300 BCE",
        "DeathDate": "unknown",
        "KeyWorks": ["Euclidean Geometry", "Elements"]
    },
    "Pythagoras": {
        "Description": "Ancient Greek mathematician and philosopher known for the Pythagorean theorem and contributions to number theory.",
        "BirthDate": "570 BCE",
        "DeathDate": "495 BCE",
        "KeyWorks": ["Pythagorean Theorem", "Numerical Mysticism"]
    },
    "Srinivasa Ramanujan": {
        "Description": "Indian mathematician who made significant contributions to number theory, infinite series, and continued fractions despite limited formal training.",
        "BirthDate": "1887-12-22",
        "DeathDate": "1920-04-26",
        "KeyWorks": ["Ramanujan Prime", "Partitions", "Modular Forms"]
    },
    "Alan Turing": {
        "Description": "British mathematician known as the father of computer science, instrumental in cracking the Enigma code during World War II.",
        "BirthDate": "1912-06-23",
        "DeathDate": "1954-06-07",
        "KeyWorks": ["Turing Machine", "Artificial Intelligence", "Cryptography"]
    },
    "Ada Lovelace": {
        "Description": "English mathematician considered the first computer programmer for her work on Charles Babbage's Analytical Engine.",
        "BirthDate": "1815-12-10",
        "DeathDate": "1852-11-27",
        "KeyWorks": ["First Algorithm", "Computing"]
    },
    "Blaise Pascal": {
        "Description": "French mathematician known for Pascal's Triangle, contributions to probability theory, and early work on calculating machines.",
        "BirthDate": "1623-06-19",
        "DeathDate": "1662-08-19",
        "KeyWorks": ["Pascal's Triangle", "Probability Theory", "Pascal's Law"]
    },
    "Hypatia": {
        "Description": "Greek mathematician, philosopher, and astronomer; one of the earliest female mathematicians in recorded history.",
        "BirthDate": "360 CE",
        "DeathDate": "415 CE",
        "KeyWorks": ["Conic Sections", "Astronomy", "Philosophy"]
    },
    "Andrew Wiles": {
        "Description": "British mathematician who solved Fermat's Last Theorem, a problem that had been unsolved for over 350 years.",
        "BirthDate": "1953-04-11",
        "DeathDate": "N/A",
        "KeyWorks": ["Fermat's Last Theorem", "Elliptic Curves"]
    },
    "John von Neumann": {
        "Description": "Hungarian-American mathematician known for his work in quantum mechanics, game theory, and computer science.",
        "BirthDate": "1903-12-28",
        "DeathDate": "1957-02-08",
        "KeyWorks": ["Game Theory", "Von Neumann Architecture", "Set Theory"]
    }
}

# constant pi value
pi_value = 3.141592653589793

# keprekar's constant
kaprekar_constant = 6174

# calculates square root of a number
def square_root(number):
 square_root = number ** 0.5

 return square_root

# calculates cube root of a number
def cube_root(number):
 return number ** 0.3333333333333333

# calculates square of a number
def square(number):
 square = number ** 2

 return square

# calculates cube of the number
def cube(number):
 return number ** 3

# calculates that the number is perfect square or not
def is_perfect_square(number):
 return number ** 0.5 == int(number ** 0.5)

# calculates that the cube is perfect cube or not
def is_perfect_cube(number):
 return number ** 0.3333333333333333 == int(number ** 0.3333333333333333)

# calculates hypotenus length of right angle tringle
def hypotenus(x,y):
 hypotenus = (x ** 2 + y ** 2) ** 0.5

 return hypotenus

# converts radians to degrees
def radians_to_degrees(radians):
 degrees = radians * (180 / pi_value)

 return degrees

# converts degrees to radians
def degrees_to_radians(degrees):
 radians = degrees * (pi_value / 180)

 return radians

# calculates sine
def sine(opposite,hypotenus):
 sine = opposite / hypotenus

 return sine

# calculates cosine
def cosine(adjecent,hypotenus):
 cosine = adjecent / hypotenus

 return cosine

# triangle detection using angle measures
def is_it_triangle(x,y,z):
 is_it_triangle = x + y + z == 180

 return is_it_triangle

# finds the base raised to a given power 
def base(exponent,value):
 base = 0
 number = 0

 while number > 1 or number == 0:
  if number == 0:
   number = value / exponent
   base += 1

  else:
   number = number / exponent
   base += 1

 if base ** exponent == value:
  return base

 else:
  raise ValueError('no base found for {} and {}'.format(exponent,value))

# calculates circumfrence
def circumfrence(diameter):
 circumfrence = pi_value * diameter

 return circumfrence

# calculates circle area
def circle_area(radius):
 circle_area = pi_value * radius ** 2

 return circle_area

# calculates diameter using radius
def diameter(radius):
 diameter = radius * 2

 return diameter

# calculates radius using diameter
def radius(diameter):
 radius = diameter / 2

 return radius

# generates pythogorean triplets of a number
def get_pythogorean_triplets(number):
 triplet = '{} square + {} square = {} square'.format(number * 2,number ** 2 - 1,number ** 2 + 1)

 return triplet

# detects that the number is even number
def is_it_even_number(number):
 is_it_even_number = number % 2 != 0

 return is_it_even_number

# calculates triangle area
def triangle_area(base,height):
 triangle_area = 0.5 * base * height

 return triangle_area

# calculates paralellogram area
def paralellogram_area(base,height):
 paralellogram_area = base * height

 return paralellogram_area

# calculates rectangle perimeter
def rectangle_perimeter(length,breadth):
 rectangle_perimeter = length * 2 + breadth * 2

 return rectangle_perimeter

# calculates rectangle area
def rectangle_area(length,breadth):
 rectangle_area = length * breadth

 return rectangle_area

# calculates paralellogram perimeter
def paralellogram_perimeter(base,height):
 paralellogram_perimeter = base * 2 + height * 2

 return paralellogram_perimeter

# calculates triangle perimeter
def triangle_perimeter(s1,s2,s3):
 triangle_perimeter = s1 + s2 + s3

 return triangle_perimeter

# detects that the number is negitive integer
def is_it_negitive_integer(number):
 is_it_negitive_integer = number < 0

 return is_it_negitive_integer

# gets multiplication table of a number
def table(number):
 table = ''
 
 for i in range(10):
  table += '{} x {} = {}\n'.format(number,i + 1,(i + 1) * number)
 
 return table

# gets additive inverse of a number
def aditive_inverse(number):
 aditive_inverse = number * (-1)

 return aditive_inverse

# gets factors of a number
def factors(number):
 return [num for num in range(1, number + 1) if number % num == 0]

# gets hcf of 2 numbers
def hcf(first_number,second_number):
 factors1 = factors(first_number)
 factors2 = factors(second_number)

 common_factors = []

 for factor in factors1:
  if factor in factors2:
   common_factors.append(factor)

 hcf = max(common_factors)

 return hcf

# detects that number is prime number
def is_it_prime_number(number):
 is_it_prime_number = len(factors(number)) == 2
 
 return is_it_prime_number

# calculates prime factors of the numbers
def prime_factorize(num):
 minimum_prime_number_divisible = 0
 prime_factors = []

 while num > 1:
  minimum_prime_number_divisible = min([n for n in factors(num) if is_it_prime_number(n)])
  prime_factors.append(minimum_prime_number_divisible)
  num //= minimum_prime_number_divisible

 return prime_factors

# gets factorial of a number (without recursion)
def factorial(number):
 factorial = number
 
 if number == 1:
  return 1

 else:
  while number != 1:
   number -= 1
   factorial *= number

  return factorial

# calculates the percentage
def percentage(consumption,total):
 percentage = consumption / total * 100

 return percentage

# convertes km to meter
def km_to_meter(km):
 meter = float(km * 1000)

 return meter

# convertes meter to km
def meter_to_km(meter):
 km = meter / 1000

 return km

# convertes meter to cm
def meter_to_cm(meter):
 cm = float(meter * 100)

 return cm

# convertes cm to meter
def cm_to_meter(cm):
 meter = cm / 100

 return meter

# convertes cm to mm
def cm_to_mm(cm):
 mm = float(cm * 10)

 return mm

# convertes mm to cm
def mm_to_cm(mm):
 cm = mm / 10

 return cm

# gets the standard form of number (small numbers of decimal form) number to be inputted in string
def standard_form(num):
 if Decimal(num) > Decimal('0.0') and Decimal(num) < Decimal('1.0') and str(num) == num:
  exponent = 0

  while int(float(num)) == 0:
   num = Decimal(num) * Decimal('10.0')
   num = num.normalize()
   exponent -= 1

  return f"{num} * 10 ** {exponent}"

 else:
  raise ValueError('the number type might not be string or the number value might not be decimal')

# split digits of integer into a list (without any conversions)
def split_into_digits(num):
 digits = []

 while num > 0:
  digits.append(num % 10)
  num = (num - num % 10) // 10

 return digits[::-1]

# combines array of digits into number (without any conversions)
def combine_digits(digits):
 num = 0

 for digit in digits:
  num = num * 10 + digit

 return num

# gets number of iterations to applied on number for kaprekar's routine
def iterations_of_keprekar_routine(num):
 iterations = 0
 
 while num != kaprekar_constant:
  splitted_digits_of_number = split_into_digits(num)
  ascending_digits = []
  
  while splitted_digits_of_number:
   ascending_digits.append(max(splitted_digits_of_number))
   splitted_digits_of_number.remove(max(splitted_digits_of_number))
  
  num = abs(combine_digits(ascending_digits) - combine_digits(ascending_digits[::-1]))

  if num > 0:
   iterations += 1

  else:
   raise ValueError('Is a repdigit number')

 return iterations
  
# check weather integer is palindrome
def is_palindrome(num):
 return split_into_digits(num) == digits[::-1]

# seprates number into commas (using international system)
def seperate_digits_of_number(n, seperator = ','):
 commas_seperated_number = ''
 digits_added = 0

 while n > 0:
  commas_seperated_number += str(n % 10)
  n = (n - n % 10) // 10
  digits_added += 1

  if digits_added == 3:
   commas_seperated_number += seperator
   digits_added = 0

 commas_seperated_number = commas_seperated_number[::-1]
     
 if len(commas_seperated_number) > 0:
  if commas_seperated_number[0] == seperator:
   return commas_seperated_number[1:len(commas_seperated_number)]

  else:
   return commas_seperated_number

 else:
  return "0"

# gets the number of cuts in a circle to break circle to number of pieces
def minimum_cuts(number_of_pieces_to_break):
 if number_of_pieces_to_break > 1:
  return number_of_pieces_to_break // 2 if number_of_pieces_to_break % 2 == 0 else number_of_pieces_to_break

 else:
  return 0

# gets the type of triangle (returns none in string if the sides do not form triangle)
def type_of_triangle(side1, side2, side3):
 if side1 + side2 > side3 and side2 + side3 > side1  and side1 + side3 > side2:
  if side1 == side2 and side2 == side3:
   return "equilateral"

  if side1 != side2 and side2 != side3 and side1 != side3:
   return "scalene"

  if side1 == side2 or side2 == side3 or side1 == side3:
   return "isosceles"

 else:
  return "none"

# gets the expanded form of a number
def expanded_form(number):
 expanded_form = []
 number_position = 0

 while number > 0:
  expanded_form.append(number % 10 * 10 ** number_position)
  number = (number - number % 10) // 10
  number_position += 1

 return expanded_form

# gets the lcm of the number
def lcm(number1, number2):
 return (number1 * number2) // hcf(number1, number2)

# performs all operations on fraction and has some more features of fraction
class Fraction:
 def __init__(self, fraction):
  self.numerator = int(fraction.split('/')[0])
  self.denominator = int(fraction.split('/')[1])

 # simplifies the fraction
 def simplify(self):
  hcf_of_fraction = hcf(self.numerator, self.denominator)

  return Fraction(f'{self.numerator // hcf_of_fraction}/{self.denominator // hcf_of_fraction}')

 # checks weather the fraction is simplified
 def is_simplified(self):
  hcf_of_fraction = hcf(self.numerator, self.denominator)

  return hcf_of_fraction == 1

 # reciprocals the fraction
 def reciprocal(self):
  return Fraction(f'{self.denominator}/{self.numerator}')

 # converts fraction object to string
 def to_string(self):
  return f'{self.numerator}/{self.denominator}'

 # adds two fractions
 def __add__(self, other):
  lcm_of_denominators = lcm(self.denominator, other.denominator)

  numerator1, numerator2 = lcm_of_denominators // self.denominator * self.numerator, lcm_of_denominators // other.denominator * other.numerator

  return Fraction(f'{numerator1 + numerator2}/{lcm_of_denominators}')

 # subtracts two fractions
 def __sub__(self, other):
  lcm_of_denominators = lcm(self.denominator, other.denominator)

  numerator1, numerator2 = lcm_of_denominators // self.denominator * self.numerator, lcm_of_denominators // other.denominator * other.numerator

  return Fraction(f'{numerator1 - numerator2}/{lcm_of_denominators}')

 # multiplies two fractions
 def __mul__(self, other):
  return Fraction(f'{self.numerator * other.numerator}/{self.denominator * other.denominator}')

 # divides two fractions
 def __truediv__(self, other):
  return Fraction(f'{self.numerator * other.denominator}/{self.denominator * other.numerator}')

# has three features related to (x, y) coordinates
class Point:
 def __init__(self, x, y):
  self.x = x
  self.y = y

 # calculates distance and direction between two points
 def __sub__(self, other):
  direction = ''
  distance = square_root(square(other.x - self.x) + square(self.y - other.y))

  if other.x > self.x:
   direction += 'N'

  if other.x < self.x:
   direction += 'S'

  if other.y > self.y:
   direction += 'E'

  if other.y < self.y:
   direction += 'W'
  
  return {'distance': distance, 'direction':direction, 'MidPoint': Point((self.x + other.x) / 2, (self.y + other.y) / 2)}

 # converts point into tuples
 def to_tuple(self):
  return (self.x, self.y)

# has all the features related to algebric or numeric expressions
class Expression:
 def __init__(self, expression):
  self.expression = expression

 # splits expression into terms
 def split_into_terms(self):
  expression = self.expression.replace(' ', '')
 
  terms_list = []

  for charecter in expression:
   if charecter.isalpha() or charecter.isdigit() or charecter == '/' or charecter == '*':
    if len(terms_list) > 0:
     terms_list[len(terms_list) - 1] += charecter

    else:
     terms_list.append(charecter)

   else:
    terms_list.append(charecter)

  return terms_list

 # checks that the 2 terms are like terms or not
 def __eq__(self, other):
  if len(self.split_into_terms()) == 1 and len(other.split_into_terms()) == 1: 
   variables_of_term1 = ''
   variables_of_term2 = ''

   for charecter in self.split_into_terms()[0]:
    if charecter.isalpha():
     variables_of_term1 += charecter

   for charecter in other.split_into_terms()[0]:
    if charecter.isalpha():
     variables_of_term2 += charecter

   return variables_of_term1 == variables_of_term2 and any(variables_of_term1) and any(variables_of_term2)

 # identifies that the expression is algebric or not
 def is_algebric_expression(self):
  for term in self.split_into_terms():
   for charecter in term:
    if charecter.isalpha():
     return True

  return False

 # gets the coefficient of the constant or a variable
 def coefficient(self, variable_or_constant):
  if variable_or_constant.isalpha() or variable_or_constant.isdigit():
   if self.expression.index(variable_or_constant) == len(self.expression) - 1:
    coefficient = self.expression[self.expression.index(variable_or_constant) - 1]

   elif self.expression.index(variable_or_constant) == 0:
    coefficient = self.expression[self.expression.index(variable_or_constant) + 1]

   else:
    coefficient = self.expression[self.expression.index(variable_or_constant) - 1] + self.expression[self.expression.index(variable_or_constant) + 1]

  coefficient = '-1' if coefficient == '-' else '1' if coefficient == '+' else coefficient

  return coefficient.replace('+', '') if coefficient.startswith('+') else coefficient

 # splits algebric expression into factors
 def factorize(self):
  factors_of_expression = []
  
  for term in self.split_into_terms():
   for char in term:
    if char == '-':
     factors_of_expression.append(-1)

    elif char.isdigit():
     factors_of_expression += prime_factorize(int(char))

    elif char.isalpha():
     factors_of_expression.append(char)

  return factors_of_expression

 # common factor of two terms (without brackets)
 def find_common_factor(self, other):
  if len(self.split_into_terms()) == 1 and len(other.split_into_terms()) == 1:
   factors1 = self.factorize()
   factors2 = other.factorize()

   common_factors = []

   for factor in factors1:
    if factor in factors2 and factor not in common_factors:
     common_factors.append(factor)
     
   return common_factors

 # expands an exprssion (with brackets)
 def expand_expression(self):
  self.expression = self.expression.replace(' ', '')
  
  expression = ''

  if self.expression[0] == '(':
   common = self.expression.split(')(')[0] + ')'
   expression_inside_paranthesis = self.expression.split(')(')[1].replace(')', '')

  else:
   common = self.expression.split('(')[0]
   expression_inside_paranthesis = self.expression.split('(')[1].replace(')', '')

  for term in Expression(expression_inside_paranthesis).split_into_terms():
   if not term.startswith('+') and not term.startswith('-'):
    if term.isalpha():
     expression += common + term

    elif common.isalpha():
     expressiom += term + common
     
    else:
     expression += common + '*' + term

   else:
    if term.replace(term[0], '').isalpha():
     expression += term[0] + common + term.replace(term[0], '')
     
    elif common.isalpha():
     expression += term[0] + common + term.replace(term[0], '')

    else:
     expression += term[0] + common + '*' + term.replace(term[0], '') 
     
  return Expression(expression)
    
# has few features related to time like convert it to text representation or convert 24 hour time to 12 hour time or calculate difference between two times
class Time:
 def __init__(self, time):
  minute = int(time.split(':')[1])
  hour = int(time.split(':')[0])

  if hour == 0:
   self.hour = 24

  if hour <= 24 and minute <= 59 and minute >= 0:
   self.hour = hour
   self.minute = minute

  else:
   raise ValueError('invalid time')

 # converts time to text
 def convert_to_text(self):
  past = ''
  to = ''
  
  if self.minute == 15:
   past = 'quater'

  elif self.minute == 30:
   past = 'half'

  elif self.minute >= 45:
   if self.minute == 45:
    to = 'quater'

   else:
    to = number_names.get(60 - self.minute)
    print(number_names.get(60 - self.minute))

  elif self.minute > 0:
   past = number_names.get(self.minute)

  if past:
   return f'{past} past {number_names.get(self.hour)}'

  elif to:
   return f'{to} to {number_names.get(self.hour + 1)}'

  elif not past and not to:
   return f'{number_names.get(self.hour)} o clock'

 # converts 24 hour clock time to 12 hour clock time
 def twelve_hour_time(self):
  if self.hour < 13:
   if self.minute < 9:
    return f'{self.hour}:0{self.minute} AM'

   else:
    return f'{self.hour}:{self.minute} AM'

  else:
   if self.minute < 9:
    return f'{self.hour - 12}:0{self.minute} PM'

   else:
    return f'{self.hour - 12}:{self.minute} PM'

 # gets difference between two times (in minutes or hours or secs)
 def __sub__(self, other):
  mins1 = self.hour * 60 + self.minute
  mins2 = other.hour * 60 + other.minute

  return mins1 - mins2

# creates list of intresting mathematicians
def intresting_mathematicians_list():
 return [mathematician for mathematician in mathematicians]

# gets the description of the mathematician
def description(mathematician_name):
 return mathematicians[mathematician_name]['Description']

# gets the keyworks of mathematicians
def keyworks(mathematician_name):
 return mathematicians[mathematician_name]['KeyWorks']

# gets the lifespan of mathematician
def lifespan(mathematician_name):
 birthdate = mathematicians[mathematician_name]['BirthDate']
 deathdate = mathematicians[mathematician_name]['DeathDate']

 splitted_birthdate = birthdate.split('-')
 splitted_deathdate = deathdate.split('-')

 if len(splitted_birthdate) > 1 and len(splitted_deathdate) > 1:
  year1 = int(splitted_deathdate[0])
  year2 = int(splitted_birthdate[0])

  return year1 - year2 + (int(splitted_birthdate[1]) <= int(splitted_deathdate[1]) or int(splitted_birthdate[2]) <= int(splitted_deathdate[2]))

 else:
  year1 = int(splitted_birthdate[0].replace('BCE', '').replace('CE', ''))
  year2 = int(splitted_deathdate[0].replace('BCE', '').replace('CE', ''))

  return year2 - year1

