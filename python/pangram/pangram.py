import string

def is_pangram (my_string):
    count = 0
    set_input = sorted(set(my_string.lower()))
    for char in set_input:
        if char in list(string.ascii_lowercase):
            count += 1
    return count == 26


    
