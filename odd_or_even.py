# 2nd exericise
# Checking if number meets the requirements

def can_i_divide (num, num2):
    if num % num2 == 0:
        return True
    else:
        return False


num = int(input('Enter number >>> '))
num2 = int(input('Enter second number >>> '))
if num % 2 == 0:
    print('Number is even! :)')
    if num % 4 == 0:
        print('Number is also multiple of 4')
else:
    print('Number is odd! :(')

if can_i_divide(num, num2):
    print(f'{num} can be divided by {num2}')
else:
    print(f'{num} cannot be divided by {num2}')