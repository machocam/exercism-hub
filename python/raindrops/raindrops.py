def convert(number):
    result = ""
    sounds = [(3, "Pling"), (5, "Plang"), (7, "Plong")]
    for (factor, sound) in sounds: 
        if number % factor == 0: 
            result += sound
    if result == "": 
        return str(number)
    else:
        return result

