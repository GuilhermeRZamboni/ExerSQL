saldo = 0
def menu():
    print("------MENU------\n1-sacar\n2-depositar\n3-mostrar saldo\n4-sair")


def saque():
    valor = float(input("Digite o valor a ser sacado: "))
    global saldo
    if valor > saldo:
        print("Saldo insuficiente")
    else:
        saldo -= valor
        print("Saque realizado com sucesso\nVoltando ao menu...")

def deposito():
    valor = float(input("Digite o valor a ser depositado: "))
    global saldo
    saldo += valor
    print("Depósito realizado com sucesso\nVoltando ao menu...")

def mostrar_saldo():
    print(f"Seu saldo é de: R$ {saldo:,.2f}")

def validar_opcao(opcao):
    if opcao.isdigit():
        opcao = int(opcao)
        return opcao
    return "Opção inválida!"
