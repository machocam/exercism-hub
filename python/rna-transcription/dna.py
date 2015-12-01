def to_rna (input_data):
    transcribe_data = {
        "C": "G",
        "G": "C",
        "T": "A",
        "A": "U"
        }
    rna_output = ""
    for char in input_data:
        rna_output += transcribe_data[char]
    return rna_output