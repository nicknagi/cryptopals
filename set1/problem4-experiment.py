def main():
    from utils import single_char_key_search

    with open('problem4.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    highest_score = -1
    best_result = ''

    for c in content:
        result = single_char_key_search(c)
        if result[1] > highest_score:
            highest_score = result[1]
            best_result = result[0]

    print(best_result.decode())
if __name__ == '__main__':
    main()