def main():
    from utils import single_char_key_search

    with open('problem4.txt') as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content] 
    for c in content:
        print(single_char_key_search(c))
if __name__ == '__main__':
    main()