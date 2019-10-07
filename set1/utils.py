def hex_to_base64(hex_input):
    from data_utils import generate_hex_to_binary_mapping, generate_binary_to_base64_mapping

    if len(hex_input) == 0:
        return ''

    hex_to_bin = generate_hex_to_binary_mapping()
    hex_string_to_binary_string = ''
    binary_chunks_to_convert = []

    for char in hex_input:
        hex_string_to_binary_string+=hex_to_bin[char]
    
    for chunk in range(0,len(hex_string_to_binary_string),24):
        if chunk + 24 < len(hex_string_to_binary_string):
            binary_chunks_to_convert.append(hex_string_to_binary_string[chunk:chunk+24])
        else:
            binary_chunks_to_convert.append(hex_string_to_binary_string[chunk:])

    base64_final_string = ''

    for chunk in binary_chunks_to_convert[:-1]:
        base64_final_string+=_base64_for_chunk(chunk)
    
    final_chunk = binary_chunks_to_convert[-1]
    base64_final_string+=_base64_for_chunk(final_chunk)

    return base64_final_string

def hex_string_xor(string1, string2):
    from data_utils import generate_hex_to_binary_mapping, _num_to_binary, generate_binary_to_hex_mapping

    if len(string1) != len(string2):
        print(f'Strings of unequal size {len(string1)} != {len(string2)}')
        raise AssertionError()

    bin_to_hex = generate_binary_to_hex_mapping()
    
    xored_bin = int(string1,16) ^ int(string2,16)
    xored_bin_string = _num_to_binary(xored_bin, len(string1)*4)

    xored_hex_string = ''
    for i in range(0,len(xored_bin_string),4):
        xored_hex_string+=bin_to_hex[xored_bin_string[i:i+4]]
    
    return xored_hex_string

# untested code
def get_english_score(input_bytes):
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])

# untested code
def single_char_xor(input_bytes, char_value):
    output_bytes = b''
    for byte in input_bytes:
        output_bytes += bytes([byte ^ char_value])
    return output_bytes

def _base64_for_chunk(chunk):
    from data_utils import generate_binary_to_base64_mapping
    bin_to_base64 = generate_binary_to_base64_mapping()

    chunk_modified = chunk
    base64_string = ''

    chunk_modified+='0'*{8: 4, 16: 2, 24: 0}[len(chunk)]

    for index in range(0,len(chunk_modified),6):
        if index == len(chunk_modified):
            continue
        base64_string+=bin_to_base64[chunk_modified[index:index+6]]

    if len(base64_string) == 2:
        base64_string+='=='
    elif len(base64_string) == 3:
        base64_string+='='
    return base64_string