def generate_hex_to_binary_mapping():
    import string

    hex_alphabet = string.digits + 'abcdef'
    return _create_mapping_from_alphabet(hex_alphabet,4,binary_to_alphabet=False)

def generate_binary_to_base64_mapping():
    import string

    base64_alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
    return _create_mapping_from_alphabet(base64_alphabet,6)

def _create_mapping_from_alphabet(input_alphabet, bin_padding, binary_to_alphabet=True):
    map = {}
    for counter,alphabet in enumerate(input_alphabet):
        counter_binary = "{0:0{1}b}".format(counter,bin_padding)
        if binary_to_alphabet:
            map[counter_binary] = alphabet
        else:
            map[alphabet] = counter_binary
    return map