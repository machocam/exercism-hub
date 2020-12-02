def square(number):
    if number not in range(1, 65):
       raise ValueError("That square doesn't exist on the board")
    else: 
        return 2**(number-1)


def total():
    return sum(square(number) for number in range(1,65))

