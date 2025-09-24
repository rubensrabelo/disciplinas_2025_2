import base64


def decrypt(ciphertext_b64: str, key: str) -> str:
    """
    Aplica a cifra de Vigenère (ASCII 0–255) para descriptografar o texto.
    A entrada deve ser uma string Base64 gerada por encrypt().
    """
    encrypted_bytes = base64.b64decode(ciphertext_b64)
    key_length = len(key)
    result = []

    for i, byte_value in enumerate(encrypted_bytes):
        key_value = ord(key[i % key_length])
        decrypted_value = (byte_value - key_value) % 256
        result.append(chr(decrypted_value))

    return "".join(result)
