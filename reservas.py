from clientes import clientes
from quartos import quartos

reservas = []

def criar_reserva():
    if not clientes:
        print("Não há clientes registados!")
        return
    nome = input("Nome do cliente: ")
    cliente = next((c for c in clientes if c["nome"] == nome), None)
    if not cliente:
        print("Cliente não encontrado.")
        return

    disponiveis = [q for q in quartos if q["disponivel"]]
    if not disponiveis:
        print("Nenhum quarto disponível.")
        return

    print("\nQuartos disponíveis:")
    for q in disponiveis:
        print(f"{q['numero']} - {q['tipo']}")
    num = int(input("Número do quarto: "))

    quarto = next((q for q in quartos if q["numero"] == num and q["disponivel"]), None)
    if quarto:
        quarto["disponivel"] = False
        reservas.append({"cliente": cliente["nome"], "quarto": num})
        print(f"Reserva criada para {cliente['nome']} no quarto {num}.")
    else:
        print("Quarto inválido ou ocupado.")

def cancelar_reserva():
    if not reservas:
        print("Não há reservas.")
        return
    nome = input("Nome do cliente: ")
    reserva = next((r for r in reservas if r["cliente"] == nome), None)
    if reserva:
        quarto = next(q for q in quartos if q["numero"] == reserva["quarto"])
        quarto["disponivel"] = True
        reservas.remove(reserva)
        print(f"Reserva de {nome} cancelada.")
    else:
        print("Reserva não encontrada.")

def listar_reservas():
    if not reservas:
        print("Nenhuma reserva registada.")
    else:
        print("\n--- Reservas ---")
        for r in reservas:
            print(f"Cliente: {r['cliente']} | Quarto: {r['quarto']}")

def menu_reservas():
    while True:
        print("\n=== Gestão de Reservas ===")
        print("1. Criar Reserva")
        print("2. Cancelar Reserva")
        print("3. Listar Reservas")
        print("0. Voltar")

        op = input("Escolha se quer: ")
        if op == "1":
            criar_reserva()
        elif op == "2":
            cancelar_reserva()
        elif op == "3":
            listar_reservas()
        elif op == "0":
            break
        else:
            print("Opção inválida.")