def generate_random_base64_string():
    import random, string, base64
    alphabet = string.ascii_uppercase + string.ascii_lowercase
    random_string = ''.join(random.choice(alphabet) for n in range(int(random.randint(1,10000) * 2)))
    return base64.b64encode(bytes(random_string, 'utf-8'))