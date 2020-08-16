# quicksort algorithm in python


def partition(arr, start, end):
    i = start - 1
    pivot = arr[end]

    for j in range(start, end):
        if arr[j] <= pivot:
            i +=1 
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1],arr[end] = arr[end],arr[i+1]
    return(i+1)



def quicksort(ls, start, end):
    if start < end:
        pivot = partition(ls,start,end)
        quicksort(ls, start, pivot - 1)
        quicksort(ls, pivot + 1, end)




list1 = [5, 3, 8, 4, 6, 3, 2]
quicksort(list1, 0, len(list1) - 1)
print(list1)