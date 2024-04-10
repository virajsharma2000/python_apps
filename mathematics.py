pi_value = 3.141592653589793

def square_root(number):
 square_root = number ** 0.5

 return square_root

def square(number):
 square = number ** 2

 return square

def hypotenus(x,y):
 hypotenus = (x ** 2 + y ** 2) ** 0.5

 return hypotenus

def radians_to_degrees(radians):
 
 degrees = radians * (180 / pi_value)

 return degrees

def degrees_to_radians(degrees):
 radians = degrees * (pi_value / 180)

 return radians

def sine(opposite,hypotenus):
 sine = opposite / hypotenus

 return sine

def cosin(adjecent,hypotenus):
 cosin = adjecent / hypotenus

 return cosin

def is_it_triangle(x,y,z):
 is_it_triangle = x + y + z == 180

 return is_it_triangle

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

def circumfrence(diameter):
 circumfrence = pi_value * diameter

 return circumfrence

def circle_area(radius):
 circle_area = pi_value * radius ** 2

 return circle_area

def diameter(radius):
 diameter = radius * 2

 return diameter

def radius(diameter):
 radius = diameter / 2

 return radius

def get_pythogorean_triplets(number):
 triplet = '{} square + {} square = {} square'.format(number * 2,number ** 2 - 1,number ** 2 + 1)

 return triplet

def is_it_even_number(number):
 is_it_even_number = number % 2 != 0

 return is_it_even_number

def triangle_area(base,height):
 triangle_area = 0.5 * base * height

 return triangle_area

def paralellogram_area(base,height):
 paralellogram_area = base * height

 return paralellogram_area

def rectangle_perimeter(length,breadth):
 rectangle_perimeter = length * 2 + breadth * 2

 return rectangle_perimeter

def rectangle_area(length,breadth):
 rectangle_area = length * breadth

 return rectangle_area

def paralellogram_perimeter(base,height):
 paralellogram_perimeter = base * 2 + height * 2

 return paralellogram_perimeter

def triangle_perimeter(s1,s2,s3):
 triangle_perimeter = s1 + s2 + s3

 return triangle_perimeter

def is_it_negitive_integer(number):
 is_it_negitive_integer = number < 0

 return is_it_negitive_integer

def table(number):
 table = ''
 
 for i in range(10):
  table += '{} x {} = {}\n'.format(number,i + 1,(i + 1) * number)
 
 return table

def aditive_inverse(number):
 aditive_inverse = number * (-1)

 return aditive_inverse



