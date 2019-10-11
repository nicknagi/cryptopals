def main():
    from utils import base64_to_binary, hamming_distance, single_char_key_search
    import numpy as np
    
    with open('data/problem6.txt') as f:
        content = f.read()
    content = content.replace('\n','')

    binary_data = base64_to_binary(content) #could be problem, even though tested

    # might need to try more key sizes
    min_info = []
    for keysize in range(2,41):
        distance = hamming_distance(binary_data[:keysize*8], binary_data[keysize*8: keysize*2*8]) / keysize
        min_info.append((keysize, distance))
    
    best_key_sizes = sorted(min_info, key=lambda x: x[1])

    potential_keys = []
    
    for keysize_data in best_key_sizes:
        potential_key = ''
        key_size = keysize_data[0]
        keysize_num_bits = key_size * 8
        print(f'Trying Keysize {key_size} With AVG Hamming Distance Of {keysize_data[1]}')

        if len(binary_data)%(keysize_num_bits) != 0:
            binary_data_divisible = binary_data[:-(len(binary_data)%(keysize_num_bits))]
        else:
            binary_data_divisible = binary_data

        splatted_binary_data = np.asarray([*binary_data_divisible]) #could be problem
        numpy_binary_data = np.reshape(splatted_binary_data,(int(len(splatted_binary_data)/keysize_num_bits), keysize_num_bits)) #could be problem

        for block_start in range(0,keysize_num_bits-7,8): 
            binary_string_builder = ''
            block = numpy_binary_data[:,block_start:block_start+8] # automate this and everything following

            splatted_bin = list(block)

            for list_of_bytes in splatted_bin:
                binary_string_builder += ''.join(list_of_bytes)
            
            from data_utils import generate_binary_to_hex_mapping
            bin_to_hex = generate_binary_to_hex_mapping()

            hex_string = ''
            for i in range(0,len(binary_string_builder),4):
                hex_string+=bin_to_hex[binary_string_builder[i:i+4]]

            potential_key += single_char_key_search(hex_string)[2]
        potential_keys.append(potential_key)
    
    # print(potential_keys)

    final = []
    from encryption import repeating_key_xor
    for key in potential_keys:
        from utils import get_english_score

        final.append((key, get_english_score(bytes(key, 'ascii'))))
    
    best_shit = sorted(final, key=lambda x: x[1], reverse=True)
    # print(repeating_key_xor('Terminator X: Bring the noise', content))
    
    import pprint
    pprint.pprint(best_shit)

    # Key is: Terminator X: Bring the noise



if __name__ == '__main__':
    main()