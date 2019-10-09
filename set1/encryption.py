def repeating_key_xor(key,data):
    import binascii
    from utils import hex_string_xor

    repeating_key = key * int(len(data) / len(key))
    remainder = len(data) % len(key)
    repeating_key += key[:remainder]

    a = binascii.hexlify(bytes(data, 'utf-8'))
    b = binascii.hexlify(bytes(repeating_key, 'utf-8'))

    return hex_string_xor(a,b)