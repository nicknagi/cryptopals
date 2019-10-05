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