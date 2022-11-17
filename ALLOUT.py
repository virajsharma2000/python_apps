import glob
import os

viruses_array = glob.glob('*.bat') + glob.glob('*.vbs') + glob.glob('*.exe')


number_of_viruses = len(viruses_array)


if number_of_viruses == 0:
    print(number_of_viruses,'viruses detected')
    
if number_of_viruses == 1:
    print(number_of_viruses,'virus detected')

    delete_permission = input('do you want to delete this virus: ')

    if delete_permission == 'yes':

     for viruses in viruses_array:
        os.remove(viruses)

     print('viruses deleted successfully!!')

    if delete_permission == 'no':
     exit()

if number_of_viruses > 1:
    print(number_of_viruses,'virus detected')
    
    delete_permission = input('do you want to delete these viruses: ')

    if delete_permission == 'yes':

        for viruses in viruses_array:
         os.remove(viruses)

        print('viruses deleted successfully!!')

    else:
        exit()

    
