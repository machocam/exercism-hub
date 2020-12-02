def reverse(text):
    rev_string = ""
    for char in range(len(text)-1,-1,-1):
        rev_string += text[char]
    return rev_string 


