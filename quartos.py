quartos = [
    {"numero": 11, "tipo": "single", "disponivel": True},
    {"numero": 12, "tipo": "duplo", "disponivel": True},
    {"numero": 13, "tipo": "suite", "disponivel": True}
]


def listar_quartos():
    print("\n=== Quartos ===")
    for q in quartos:
        estado = "Disponível" if q["disponivel"] else "Ocupado"
        print(f"Nº {q['numero']} | Tipo: {q['tipo']} | Estado: {estado}")

def menu_quartos():
    while True:
        print("\n=== Gestão de Quartos ===")
        print("1. Listar Quartos")
        print("0. Voltar")

        op = input("Escolha: ")
        if op == "1":
            listar_quartos()
        elif op == "0":
            break
        else:
            print("Opção inválida.")            