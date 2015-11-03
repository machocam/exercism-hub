
def word_count(string):
    a=string.lower().split()
    return { word:a.count(word) for word in a }
