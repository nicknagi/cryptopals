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
    bin_to_base64 = generate_binary_to_base64_mapping()

    for chunk in binary_chunks_to_convert[:-1]:
        base64_final_string+=bin_to_base64[chunk[:6]]
        base64_final_string+=bin_to_base64[chunk[6:12]]
        base64_final_string+=bin_to_base64[chunk[12:18]]
        base64_final_string+=bin_to_base64[chunk[18:24]]
    
    final_chunk = binary_chunks_to_convert[-1]
    last_chunk_len = len(final_chunk)

    if last_chunk_len == 8:
        final_chunk+='0000'
        base64_final_string+=bin_to_base64[final_chunk[:6]]
        base64_final_string+=bin_to_base64[final_chunk[6:12]]
        base64_final_string+='=='
    elif last_chunk_len == 16:
        final_chunk+='00'
        base64_final_string+=bin_to_base64[final_chunk[:6]]
        base64_final_string+=bin_to_base64[final_chunk[6:12]]
        base64_final_string+=bin_to_base64[final_chunk[12:18]]
        base64_final_string+='='
    else:
        base64_final_string+=bin_to_base64[final_chunk[:6]]
        base64_final_string+=bin_to_base64[final_chunk[6:12]]
        base64_final_string+=bin_to_base64[final_chunk[12:18]]
        base64_final_string+=bin_to_base64[final_chunk[18:24]]
    
    return base64_final_string

