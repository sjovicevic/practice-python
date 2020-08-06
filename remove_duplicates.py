def remove_duplicates(ls):
    ls2 = []
    duplicates = []
    for item in ls:
        if item not in duplicates:
            ls2.append(item)
        duplicates.append(item)
    return ls2
    
    

list1 = [5, 10, 1, 1, 2, 3, 4, 4, 5]
print(remove_duplicates(list1))