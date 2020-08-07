# Fun game of cows and bulls (I made it to work, I don't know how efficient it is)

import random

def game(number, guess):
    cows = 0
    bulls = 0
    for item in range(len(guess)):
        if guess[item] in list(number):
            if guess[item] == number[item]:
                cows+=1
            else:
                bulls+=1
    return cows, bulls


def create_num():
    text = ''
    for item in range(4):
        text+=(str(random.randint(0,9)))
    return text


num = '1038'
while True:
    guess = input('Enter 4 digits number >>> ')
    cows, bulls = game(num, guess)
    if cows == 4:
        print(f'Congratulations you guessed the {num} ')
        break
    print(f'{cows} cow, {bulls} bull')
