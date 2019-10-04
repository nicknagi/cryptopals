def generate_hex_to_binary_mapping():
    return {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'a': '1010',
        'b': '1011',
        'c': '1100',
        'd': '1101',
        'e': '1110',
        'f': '1111'
    }

def generate_binary_to_base64_mapping():
    import string

    base64_alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
    map = {}
    for counter,alphabet in enumerate(base64_alphabet):
        counter_binary = "{0:06b}".format(counter)
        map[counter_binary] = alphabet
    
    return map
