import re

def encode (in_string):
    counter = 1
    prev_char = ""
    out_string = ""
    for char in in_string:
        if char != prev_char:
            if prev_char: 
                if counter == 1:   #This if/else has to be here since the out_strings expected don't have "1"'s in front if there is only one of the char in question
                    out_string += prev_char
                else:
                    out_string += str(counter) + prev_char
            counter = 1
            prev_char = char
        else: 
            counter += 1
    else:
        if counter == 1:
            out_string += char
        else: 
            out_string += str(counter) + char
    return out_string
    
    
def decode (in_string): 
    out_string = ""
    multiplier = ""
    for char in in_string: 
        if char.isdigit():
            multiplier += char
        elif multiplier: #extra case had to be made for chars only shown once in a row
            out_string += int(multiplier)*char
            multiplier = ""
        else:
            out_string += char
    return out_string
