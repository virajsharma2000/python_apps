import pyperclip

word = input('Enter any word: ')

invisible_text = ''

for letters in word:

    if ord(letters) > 32:
     invisible_text += chr(ord(letters) + 32 - ord(letters))

    else:
     invisible_text += chr(ord(letters) + ord(letters) - 32)


pyperclip.copy(invisible_text)

print('invisible text copied successfully!!')
