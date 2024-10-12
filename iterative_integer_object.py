class IterativeInt:
 def __init__(self, number):
  number_array = []

  num = number

  while num > 0:
   number_array.append(num % 10)
   num = (num - num % 10) // 10

  number_array = number_array[::-1]

  self.index = 0
  self.number_array = number_array

 def __iter__(self):
  return self

 def __next__(self):
  if self.index <= len(self.number_array) - 1:
   number = self.number_array[self.index]
   self.index += 1

   return number

  else:
   raise StopIteration()



 
