from src.utils import Menu
from src import Game

def main():
    option = 2
    while True:
        try:
            if option != 1:
                Menu.generate_menu()
                option = int(input("Escolha sua opção: "))
                if option == 4:
                    break

            game = Game()
           
            while True:
                number_user: int = int(input("Digite seu número: "))

                result = game.result(number_user)

                if result == 0:
                    print("\nParabéns! Você ganhou.\n")
                elif result == 1:
                    print("\nSeu número está maior do que o valor.\n")
                else:
                    print("\nSeu número está menor do que o valor.\n")

                Menu.generate_menu()
                option = int(input("Escolha sua opção: "))
                if option in [1, 4]:
                    break
            
            if option == 4:
                break
        except Exception as e:
            print("Error: ", e)


if __name__ == "__main__":
    main()
