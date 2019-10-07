def main():
    from utils import single_char_key_search
    
    hexstring = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    print(single_char_key_search(hexstring))

if __name__ == '__main__':
    main()