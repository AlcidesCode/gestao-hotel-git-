from clientes import menu_clientes
from quartos import menu_quartos
from reservas import menu_reservas

def menu():
    while True:
        print("\n=== Sistema de gestão e reservas de hotel ===")
        print("1. Gerir Clientes")
        print("2. Gerir Quartos")
        print("3. Gerir Reservas")
        print("0. Sair do Sistema")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_clientes()
        elif opcao == "2":
            menu_quartos()
        elif opcao == "3":
            menu_reservas()
        elif opcao == "0":
            print("A sair do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")  

if __name__ == "__main__":
    menu()              
