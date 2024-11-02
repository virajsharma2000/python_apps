import ascii_art_dictnoary

def convert_to_ascii_art(text):
 ascii_art = ''

 for char in text:
  if char != ' ':
   ascii_art += ascii_art_dictnoary.ascii_art_dict.get(char) + '\n\n'

  else:
   ascii_art += '\n\n\n'

 return ascii_art
