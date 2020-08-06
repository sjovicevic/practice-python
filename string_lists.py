# Checking if the string is palindrome

user_input = input("Enter string >>> ")
print('Yes' if user_input == user_input[::-1] else 'No')