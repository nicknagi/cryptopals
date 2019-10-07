from utils import get_english_score, single_char_xor
def main():
    hexstring = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    ciphertext = bytes.fromhex(hexstring)
    potential_messages = []
    for key_value in range(256):
        message = single_char_xor(ciphertext, key_value)
        score = get_english_score(message)
        data = {
            'message': message,
            'score': score,
            'key': key_value
            }
        potential_messages.append(data)
    best_score = sorted(potential_messages, key=lambda x: x['score'], reverse=True)[0]
    for item in best_score:
        print("{}: {}".format(item.title(), best_score[item]))

if __name__ == '__main__':
    main()