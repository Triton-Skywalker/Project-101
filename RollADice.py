import random

response = input('Do you want to roll a dice?(Yes/No): ')

while response == 'Yes':
    number = random.randint(1,6)

    if number == 1:
        print('[     ]')
        print('[     ]')
        print('[  0  ]')
        print('[     ]')
        print('[     ]')
    
    elif number == 2:
        print('[     ]')
        print('[     ]')
        print('[ 0 0 ]')
        print('[     ]')
        print('[     ]')

    elif number == 3:
        print('[     ]')
        print('[ 0   ]')
        print('[  0  ]')
        print('[   0 ]')
        print('[     ]')

    elif number == 4:
        print('[     ]')
        print('[ 0 0 ]')
        print('[     ]')
        print('[ 0 0 ]')
        print('[     ]')

    elif number == 5:
        print('[     ]')
        print('[ 0 0 ]')
        print('[  0  ]')
        print('[ 0 0 ]')
        print('[     ]')

    else:
        print('[     ]')
        print('[ 000 ]')
        print('[     ]')
        print('[ 000 ]')
        print('[     ]')
    
    response = input('Do you want to play again(Yes/No): ')