def base64_to_text(b64_string):
    import base64
    return base64.b64decode(b64_string).decode()