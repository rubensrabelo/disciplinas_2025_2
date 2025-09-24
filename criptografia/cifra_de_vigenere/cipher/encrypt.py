import base64


def encrypt(plaintext: str, key: str) -> str:
    """
    Aplica a cifra de Vigenère (ASCII 0–255) para criptografar o texto.
    Retorna uma string legível (Base64) para a saída.
    """
    result = []
    key_length = len(key)

    for i, char in enumerate(plaintext):
        text_value = ord(char)
        key_value = ord(key[i % key_length])
        encrypted_value = (text_value + key_value) % 256
        result.append(encrypted_value)

    # transform list of ints into bytes
    encrypted_bytes = bytes(result)
    # encode as Base64 string
    return base64.b64encode(encrypted_bytes).decode()
