original_alphabet: dict = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
    'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
}


def produce_encryption_alphabet(key: int) -> dict:
    """
    This method produces an encrypted alphabet based on the traditional one
    :param key: the key on which encrypt the alphabet according to the caesar cipher
    :return: the shifted alphabet
    """
    shifted_alphabet = {}
    for key_dict, item_dict in original_alphabet.items():
        item: int = (original_alphabet[key_dict] + key) % 26
        for key_val, item_val in original_alphabet.items():
            if item_val == item:
                shifted_alphabet[key_val] = item_dict

    return shifted_alphabet


def produce_decryption_alphabet(encrypted_alphabet: dict, key: int) -> dict:
    """
    This method, given the encrypted alphabet, produces the correspondent decrypted one
    :param encrypted_alphabet: the alphabet to decrypt
    :param key: the key to decrypt the alphabet
    :return:
    """
    shifted_alphabet = {}
    for key_dict, item_dict in original_alphabet.items():
        item: int = (original_alphabet[key_dict] - key) % 26
        for key_val, item_val in encrypted_alphabet.items():
            if item_val == item:
                shifted_alphabet[key_val] = item_dict

    return shifted_alphabet


def encryption(message: str, key: int) -> str:
    """
    This method encrypt the message passed as argument.
    :param message: the message to encrypt
    :param key: the key used to encrypt the message
    :return: the encrypted message
    """
    shifted_alphabet: dict = produce_encryption_alphabet(key)
    for key, val in shifted_alphabet.items():
        for original_key, original_val in original_alphabet.items():
            if original_val == val:
                message.replace(original_key, key)

    return message


def decryption(message: str, key: int) -> str:
    """
    This method uses the key passed as argument to decrypt the message
    :param message: message to decrypt
    :param key: the key used to decrypt the message
    :return:
    """
    encrypted_alphabet: dict = produce_encryption_alphabet(key)
    shifted_alphabet: dict = produce_decryption_alphabet(encrypted_alphabet, key)
    for key, val in shifted_alphabet.items():
        for original_key, original_val in original_alphabet.items():
            if original_val == val:
                message.replace(original_key, key)

    return message
