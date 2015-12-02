import string

def is_pangram (my_string):
    my_string = my_string.lower()
    sum_values = 0
    string_list = sorted(my_string)
    alpha_dict = {char : 0 for char in string.ascii_lowercase}
    for char in string_list:
        if char in string.ascii_lowercase:
            alpha_dict[char] = 1
    
    for key in alpha_dict:
        sum_values += alpha_dict[key]
    return sum_values == 26
