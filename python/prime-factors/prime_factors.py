def factors(value):
    factors = []
    for i in range(2, int(value**0.5)+2): 
        while value % i == 0: 
            factors.append(i) 
            value = value / i
    if value > 1 : 
        factors.append(int(value))
    return factors





