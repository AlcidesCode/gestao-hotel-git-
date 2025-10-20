clientes = []

def registar_clientes():
    nome = input("Nome do cliente: ")
    telefone = input("Número de telemóvel: ")
    email = input("Email do cliente: ")
    nif = input("NIF do cliente: ")
    clientes.append({"nome": nome, "telefone": telefone, "email": email, "nif": nif})
    print(f"Cliente '{nome}' registado com sucesso!")


def listar_clientes():
    if not clientes:
        print("Nenhum cliente registado.")
    else:
        print("\n=== Lista de Clientes ===")
        for c in clientes:
            print(f"Nome: {c['nome']} | Telefone: {c['telefone']} | Email: {c['email']} | NIF: {c['nif']}")


def menu_clientes():
    while True:
        print("\n=== Gestão de clientes ===")
        print("1. Registar Cliente")
        print("2. Listar Clientes")
        print("0. Voltar")

        op = input("Escolha se quer: ")
        if op == "1":
            registar_clientes()
        elif op == "2":
            listar_clientes()
        elif op == "0":
            break
        else:
            print("Opção inválida.")        