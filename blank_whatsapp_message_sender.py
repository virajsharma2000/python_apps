import webbrowser

def send_blank_whatsapp_message(length_of_blank_message):
 blank_text = ''

 for i in range(length_of_blank_message):
     blank_text += '\u3164'

 webbrowser.open('https://web.whatsapp.com/send?text={}'.format(blank_text))


length_of_blank_message = int(input('length of blank message: '))

send_blank_whatsapp_message(length_of_blank_message)
