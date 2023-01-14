import random

coin_parts = ['head','tails']

head_or_tails = input('do you want head or tails: ')

flip = input('')

if flip != '':
    pass

else:
    coin_flipped = random.choice(coin_parts)

    if coin_flipped == head_or_tails:
        print('you won!!')

    else:
        print('you lost')
        
