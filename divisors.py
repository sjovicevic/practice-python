# 4th exercise
# User input gets checked which numbers can be divided with

user_input = int(input('Enter number >>> '))
list = []
for item in range(1, user_input):
    if user_input % item == 0:
        list.append(item)
print(list)

# List comprehension way of doing same task

print([item for item in range(1, user_input) if user_input % item == 0])