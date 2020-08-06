# Game of Rock, Paper, Scissors

import random

def check_winner (guess, num):
    if guess == num:
        print('Correct number! :)')
        return True
    elif guess < num:
        print('Ummmmmmmmm higher')
    else: 
        print('Ummmmmmmmm lower')


    
number = random.randint(1,10)
check = False

while True:
    user_input = int(input("What's your guess? >>> "))
    if check_winner(user_input, number):
        break
    


