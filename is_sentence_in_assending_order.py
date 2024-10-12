numbers = []

for charecter in s.split():
 if charecter.isdigit():
  numbers.append(int(charecter))

boolians_in_numbers = []

for i in range(len(numbers)):
 if not i + 1 > len(numbers) - 1:
  if numbers[i] < numbers[i + 1]:
   boolians_in_numbers.append(1)

  else:
   boolians_in_numbers.append(0)

print(0 not in boolians_in_numbers)
 
