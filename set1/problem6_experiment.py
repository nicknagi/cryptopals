def main():
    from utils import base64_to_binary, hamming_distance
    import numpy as np
    
    with open('data/problem6.txt') as f:
        content = f.read()
    content = content.replace('\n','')

    binary_data = base64_to_binary(content)

    min_info = (0,10000000)
    for keysize in range(2,41):
        distance = hamming_distance(binary_data[:keysize*8], binary_data[keysize*8: keysize*2*8]) / keysize
        if distance < min_info[1]:
            min_info = (keysize, distance)
    
    keysize_num_bits = min_info[0] * 8
    print(f'Opitmal Keysize Is {min_info[0]} With AVG Hamming Distance Of {min_info[1]}')

    print(len(binary_data))
    binary_data = binary_data[:-(len(binary_data)%(keysize_num_bits))]
    print(len(binary_data))

    binary_data = np.asarray([*binary_data])
    binary_data = np.reshape(binary_data,(int(len(binary_data)/keysize_num_bits), keysize_num_bits))
    # binary_data = np.transpose(binary_data)
    print(binary_data.shape)


if __name__ == '__main__':
    main()