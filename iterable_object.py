class NumberRange:
 def __init__(self,start,end,step):
  self.start = start
  self.end = end
  self.step = step
  
  self.current = 0

 def __iter__(self):
  return self

 def __next__(self):
  if self.current != self.end - 1:
   if self.current == 0:
    self.current += self.start

    return self.current

   else:
    self.current += self.step

    return self.current

  else:
   raise StopIteration('please stop the iteration')


for num in NumberRange(1,11,1):
 print(num)
