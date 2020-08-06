def fibonacci(n):
    ls = [0,1]
    first_index = 0
    second_index = 1
    sum = 1
    while sum + ls[second_index] - ls[first_index] < n:
        ls.append(ls[first_index]+ls[second_index])
        sum = ls[first_index]+ls[second_index]
        first_index += 1
        second_index += 1
    return ls



n = int(input('Enter number >>> '))
print(fibonacci(n))
