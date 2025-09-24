from cipher import encrypt, decrypt


def main():
    text = input("Digite o seu texto: ")
    key = input("Digite a sua chave: ")

    encrypted = encrypt(text, key)
    print("Encriptado:", encrypted)

    decrypted = decrypt(encrypted, key)
    print("Decriptado:", decrypted)


if __name__ == "__main__":
    main()
