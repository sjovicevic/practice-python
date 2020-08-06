# Game of Rock, Paper, Scissors

import random

def check_winner (in1, in2):
    if in1 == in2:
        print("It's a tie!")
    elif in1 == 'rock':
        if in2 == 'scissors':
            print('Rock wins!')
        else:
            print('Paper wins!')
    elif in1 == 'scissors':
        if in2 == 'paper':
            print('Scissors win!')
        else:
            print('Rock wins!')
    elif in1 == 'paper':
        if in2 == 'rock':
            print('Paper wins!')
        else:
            print('Scissors win!')


while True:
    choice = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
    input1 = choice[random.randint(1,3)]
    input2 = choice[random.randint(1,3)]

    print(input1, input2)
    check_winner(input1.lower(), input2.lower())

    if input('Continue? yes/no\n').lower() == 'yes':
        continue
    else:
        break


