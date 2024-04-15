# constant pi value
pi_value = 3.141592653589793

# calculates square root of a number
def square_root(number):
 square_root = number ** 0.5

 return square_root

# calculates square of a number
def square(number):
 square = number ** 2

 return square

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

# finds the base raised to a given power and power value
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
 factors1 = []
 factors2 = []
 
 num = 0

 for i in range(first_number):
  num += 1

  if first_number % num == 0:
   factors1.append(num)

 num = 0

 for i in range(second_number):
  num += 1

  if second_number % num == 0:
   factors2.append(num)

 common_factors = []

 for factor in factors1:
  if factor in factors2:
   common_factors.append(factor)

 hcf = max(common_factors)

 return hcf

# detects that number is prime number
def is_it_prime_number(number):
 factors = []
 num = 0

 for i in range(number):
  num += 1

  if number % num == 0:
   factors.append(num)

 is_it_prime_number = len(factors) == 2

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


   

  

  



