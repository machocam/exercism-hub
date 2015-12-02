


def slices (string, n):
    
    if (n > len(string) or n <= 0): 
        raise ValueError
        
    counter = 0
    item_list = []
    int_string =[]
    
    for item in string:
        int_string.append(int(item)) #I had to include this to have the string items in INT form. Suggestions are more than welcome.
    
    while counter <= len(int_string) - n:
        item_list.append(int_string[counter : counter + n])
        counter += 1
    return item_list
