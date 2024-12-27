# neccessary dependencies
from decimal import Decimal

# for letting leetcode or other coding platforms know that this module is being used to solve problems
print("Thanks for using mathematics module created by viraj sharma")

# constant pi value
pi_value = 3.141592653589793

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
 factors = []
 num = 0

 for i in range(number):
  num += 1

  if number % num == 0:
   factors.append(num)

 return factors

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

# gets factorial of a number (without recursion)
def factorial(number):
 factorial = number
 
 if number == 1:
  return 1

 else:
  while number != 1:
   number -= 1
   factorial = factorial * number

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

# check weather integer is palindrome
def is_palindrome(num):
 return split_into_digits(num) == digits[::-1]

# gets the number of cuts in a circle to break circle to number of pieces
def minimum_cuts(number_of_pieces_to_break):
 if number_of_pieces_to_break > 1:
  return number_of_pieces_to_break // 2 if number_of_pieces_to_break % 2 == 0 else number_of_pieces_to_break

 else:
  return 0

# get the type of triangle (returns none in string if the sides do not form triangle)
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




