def main():
    from utils import base64_to_binary, hamming_distance, single_char_key_search
    import numpy as np
    from encryption import repeating_key_xor_base64
    from conversion import base64_to_text
    from utils import get_english_score
    import codecs
    from data_utils import generate_binary_to_hex_mapping

    with open('data/problem6.txt') as f:
        content = f.read()
    content = content.replace('\n','')

    binary_data = base64_to_binary(content)

    min_info = []
    for keysize in range(2,41):
        num_blocks = 4
        distance = 0
        for i in range(num_blocks):
            distance += hamming_distance(binary_data[keysize*i*8:keysize*(i+1)*8], binary_data[keysize*(i+1)*8: keysize*(i+2)*8])
        for i in range(num_blocks):
            distance += hamming_distance(binary_data[keysize*i*8:keysize*(i+1)*8], binary_data[keysize*(i+2)*8: keysize*(i+3)*8])
        distance = distance / keysize
        min_info.append((keysize, distance))
    
    best_key_sizes = sorted(min_info, key=lambda x: x[1])[:3]
    potential_keys = []
    
    for keysize_data in best_key_sizes:
        potential_key = ''
        key_size = keysize_data[0]
        keysize_num_bits = key_size * 8

        if len(binary_data)%(keysize_num_bits) != 0:
            binary_data_divisible = binary_data[:-(len(binary_data)%(keysize_num_bits))]
        else:
            binary_data_divisible = binary_data

        splatted_binary_data = np.asarray([*binary_data_divisible])
        numpy_binary_data = np.reshape(splatted_binary_data,(int(len(splatted_binary_data)/keysize_num_bits), keysize_num_bits))

        for block_start in range(0,keysize_num_bits-7,8): 
            binary_string_builder = ''
            block = numpy_binary_data[:,block_start:block_start+8]

            splatted_bin = list(block)

            for list_of_bytes in splatted_bin:
                binary_string_builder += ''.join(list_of_bytes)
            
            bin_to_hex = generate_binary_to_hex_mapping()

            hex_string = ''
            for i in range(0,len(binary_string_builder),4):
                hex_string+=bin_to_hex[binary_string_builder[i:i+4]]

            potential_key += single_char_key_search(hex_string)[2]
        potential_keys.append(potential_key)

    
    potential_answers = []
    for key in potential_keys:
        decrypted_output = base64_to_text(repeating_key_xor_base64(key, content))
        english_score = get_english_score(bytes(decrypted_output, 'utf-8'))
        potential_answers.append((english_score, decrypted_output))
    
    final_answer = sorted(potential_answers, key=lambda x: x[0], reverse=True)[0]
    print(final_answer[1])

if __name__ == '__main__':
    main()