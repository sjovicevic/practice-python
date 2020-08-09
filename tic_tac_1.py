def straight(size):
    print('|' + size * (size * " " + '|'))

def dash(size):
    print(size * f" {size*'-'}")

def draw(size):
    for item in range(size):
        dash(size)
        straight(size)
    dash(size)


number = int(input("Enter table size []nxn type >>> "))
draw(number)