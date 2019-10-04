def hex_to_base64(hex_input):
    from data_utils import generate_hex_to_binary_mapping
    hex_to_bin = generate_hex_to_binary_mapping()
    # import codecs
    # return codecs.encode(codecs.decode(hex_input, "hex"), "base64").decode().strip('\n')
    hex_string_to_binary_string = ''
    binary_chunks_to_convert = []

    for char in hex_input:
        hex_string_to_binary_string+=hex_to_bin[char]
    
    for chunk in range(0,len(hex_string_to_binary_string),24):
        if chunk + 24 < len(hex_string_to_binary_string):
            binary_chunks_to_convert.append(hex_string_to_binary_string[chunk:chunk+24])
        else:
            binary_chunks_to_convert.append(hex_string_to_binary_string[chunk:])

    # for chunk in binary_chunks_to_convert:

    # Useful stuff:
    # import string
    # alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'

    # "{0:b}".format(51)
    # bin(int('110011', base=2))
