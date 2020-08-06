# Functions returns new list containing first and last element from existing list

def first_and_last(list1, list2):
    list2.append(list1[0])
    list2.append(list1[int(len(list1)-1)])
    return list2



a = [5, 10, 15, 20, 25]
b = []
print(first_and_last(a,b))

