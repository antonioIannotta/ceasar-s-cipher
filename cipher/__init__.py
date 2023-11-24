original_alphabet: dict = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
    'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
}


def _produce_encryption_alphabet(key: int) -> dict:
    shifted_alphabet = {}
    for key_dict in original_alphabet.keys():
        item = (original_alphabet[key_dict] + key) % 26
        shifted_alphabet[key_dict] = item

    return shifted_alphabet


def _produce_decryption_alphabet(key: int) -> dict:
    shifted_alphabet = {}
    for key_dict in original_alphabet.keys():
        item = (original_alphabet[key_dict] - key) % 26
        shifted_alphabet[key_dict] = item

    return shifted_alphabet


def encryption(message: str, key: int) -> str:
    shifted_alphabet = _produce_encryption_alphabet(key)
    for key, val in shifted_alphabet.items():
        for original_key, original_val in original_alphabet.items():
            if original_val == val:
                message.replace(original_key, key)

    return message


def decryption(message: str, key: int) -> str:
    shifted_alphabet = _produce_decryption_alphabet(key)
    for key, val in shifted_alphabet.items():
        for original_key, original_val in original_alphabet.items():
            if original_val == val:
                message.replace(original_key, key)

    return message
