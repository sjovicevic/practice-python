def merge_list(arr1, arr2):
    for i in range(len(arr2)):
        arr1.append(arr2[i])
    return arr1



arr1 = [1,2,3]
arr2 = [4,5,6]

print(merge_list(arr1, arr2))
