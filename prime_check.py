def is_prime(number):
    prime = True
    for item in range(2, number):
        if number % item == 0:
            prime = False
            break
    return prime



user_input = int(input('Enter number >>> '))
if is_prime(user_input):
    print('Number is prime')
else:
    print('Number is not prime')