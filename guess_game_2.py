# player thinks of a number, the computer needs to guess that number, 
# player is navigating computer by telling after each guess is the number lower or higher than that number

import random 

def game(computer_guess, my_number, start, end):
    
    try: 
        mid = (start + end) // 2

        

        
        if computer_guess == my_number:
            return computer_guess
        
        user_input = input(f'I say {computer_guess}, up or down? >>> ')
        if user_input.lower() == 'down':
            return game(random.randint(1,computer_guess), my_number, start, computer_guess - 1)
        elif user_input.lower() == 'up':
            return game(random.randint(computer_guess+1, 101), my_number, computer_guess + 1, end)
        else:
            return -1
    except:
        print("You thought of a number that is bigger than 100, you crazy fucker")

guess = random.randint(0, 101)
my_number = 96
print(f"Looks like I found your secret number, its {game(random.randint(1,100), my_number, 0, 100)}!")

