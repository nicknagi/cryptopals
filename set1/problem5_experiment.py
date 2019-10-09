def main():
    from encryption import repeating_key_xor

    key='ICE'
    input_string='Burning \'em, if you ain\'t quick and nimble I go crazy when I hear a cymbal'

    print(repeating_key_xor(key=key, data=input_string))

if __name__ == '__main__':
    main()