# 1st exercise
# Calculating from the input when will user reach 100 years old mark!

name = input("Type your name here >>> ")
age = int(input("Type your age here >>> "))
count = int(input("Type some number here >>> "))
goal = 2020 - age + 100

print(f"Hello {name}, you will be 100 years old in {goal}!\n" * count)