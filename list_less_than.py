# 3rd exercise
# Remove files from the list
# Getting to know functions better, the task was to do it in one line, which is basically line 6

def function (list, value):
    print([char for char in list if char < value])



value = int(input('Enter number >>> '))
list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
function(list, value)