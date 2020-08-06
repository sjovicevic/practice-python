import random


def create_list(list):
    list_range = random.randint(5,10)
    for item in range(list_range):
        list.append(random.randint(1,100))
    return list

list1 = []
list2 = []
list3 = []

create_list(list1)
create_list(list2)

print([item for item in list1 if item in list2])
print(list1)
print(list2)
