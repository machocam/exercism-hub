def is_armstrong_number(number):
    sum_powers = 0
    for char in str(number): 
        sum_powers += int(char)**len(str(number))
    return sum_powers == number 
    
