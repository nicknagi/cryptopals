def generate_hex_to_binary_mapping():
    import string

    hex_alphabet = string.digits + 'abcdef'
    return _create_mapping_from_alphabet(hex_alphabet,4,binary_to_alphabet=False)

def generate_binary_to_base64_mapping():
    import string

    base64_alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
    return _create_mapping_from_alphabet(base64_alphabet,6)

def generate_binary_to_hex_mapping():
    import string

    hex_alphabet = string.digits + 'abcdef'
    return _create_mapping_from_alphabet(hex_alphabet,4)

def generate_english_character_frequencies():
    return {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
# untested code
def convert_string_to_binary_string(input_string):
    return ''.join("{0:08b}".format(ord(x), 'b') for x in input_string)

def _create_mapping_from_alphabet(input_alphabet, bin_padding, binary_to_alphabet=True):
    map = {}
    for counter,alphabet in enumerate(input_alphabet):
        counter_binary = _num_to_binary(counter, bin_padding)
        if binary_to_alphabet:
            map[counter_binary] = alphabet
        else:
            map[alphabet] = counter_binary
    return map

def _num_to_binary(num_to_convert, bin_padding=0):
    return "{0:0{1}b}".format(num_to_convert,bin_padding)