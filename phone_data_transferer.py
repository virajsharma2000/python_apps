import getpass
import os
import shutil

def transfer_all_data(device_name):
    folder_exists = 'phone_data' in os.listdir('/home/{}'.format(getpass.getuser()))

    if not folder_exists:
        os.system('mkdir phone_data')

        files_and_folders = os.listdir('/media/{}/{}'.format(getpass.getuser(),device_name))

        for data in files_and_folders:
             shutil.move('/media/{}/{}/{}'.format(getpass.getuser(),phone_data_path,data),'phone_data')
            
    if folder_exists:
        files_and_folders = os.listdir('/media/{}/{}'.format(getpass.getuser(),device_name))

        for data in files_and_folders:
             shutil.move('/media/{}/{}/{}'.format(getpass.getuser(),phone_data_path,data),'phone_data')


phone_data_path = input('Enter device name attached to computer: ')

transfer_all_data(phone_data_path)
