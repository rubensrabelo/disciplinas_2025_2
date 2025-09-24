from cipher import encrypt, decrypt


def main():
    """
    Executa o fluxo principal da aplicação de cifra de Vigenère (ASCII 0–255).
    Solicita do usuário um texto e uma chave, encripta o texto em Base64
    e em seguida decripta para mostrar o texto original.
    """
    text = input("Digite o seu texto: ")
    key = input("Digite a sua chave: ")

    encrypted = encrypt(text, key)
    print("\nEncriptado:", encrypted)

    decrypted = decrypt(encrypted, key)
    print("Decriptado:", decrypted)


if __name__ == "__main__":
    main()
