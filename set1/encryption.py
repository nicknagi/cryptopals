def repeating_key_xor(key,data):
    import binascii
    from utils import hex_string_xor

    repeating_key = key * int(len(data) / len(key))
    remainder = len(data) % len(key)
    repeating_key += key[:remainder]

    a = binascii.hexlify(bytes(data, 'utf-8'))
    b = binascii.hexlify(bytes(repeating_key, 'utf-8'))

    return hex_string_xor(a,b)

def repeating_key_xor_base64(key,data):
    import binascii, base64, codecs
    from utils import hex_string_xor

    base64_data = base64.b64decode(data).hex().lower()
    
    repeating_key = key * int(len(base64_data) / len(key))
    remainder = len(base64_data) % len(key)
    repeating_key += key[:remainder]

    hex_key = binascii.hexlify(bytes(repeating_key, 'utf-8'))[:len(base64_data)]

    return codecs.encode(codecs.decode(hex_string_xor(base64_data,hex_key), 'hex'), 'base64').decode().strip()