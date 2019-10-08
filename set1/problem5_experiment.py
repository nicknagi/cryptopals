def main():
    import binascii
    from utils import hex_string_xor

    key='ICE'
    input_string='Burning \'em, if you ain\'t quick and nimble I go crazy when I hear a cymbal'

    repeating_key = key * int(len(input_string) / len(key))
    remainder = len(input_string) % len(key)
    repeating_key += key[:remainder]

    a = binascii.hexlify(bytes(input_string, 'utf-8'))
    b = binascii.hexlify(bytes(repeating_key, 'utf-8'))

    print(hex_string_xor(a,b))

if __name__ == '__main__':
    main()