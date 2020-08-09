def binary_search(ls, number, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if ls[mid] == number:
        return mid

    if ls[mid]>number:
        return binary_search(ls, number, left, mid - 1)
    else:
        return binary_search(ls, number, mid + 1, right)



list1 = [1, 3, 4, 8, 11, 22]
number = 8

print(f"Index of {number}: {binary_search(list1, number, 0, len(list1))}")
