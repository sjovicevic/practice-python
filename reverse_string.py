def reverse (text):
    ls = []
    ls = text.split(' ')
    return ls[::-1]


user_input = input('Enter sentence >>> ')
print(" ".join(reverse(user_input)))