import funcoes

compra = float(input("Digite o valor da compra: "))
print("obs: (10% = 0.1, 20% = 0.2, 30% = 0.3...): ")
desconto = float(input("Digite o valor do desconto(opcional): "))

funcoes.aplicar_desconto(compra, desconto)

print("-" * 30)
compra = float(input("Digite o valor da compra: "))
frete = float(input("Digite o valor do frete(opcional): "))

funcoes.calcular_frete(compra, frete)

print("-" * 30)

while True:
    print("menu\n1- Calcular Frete\n2-Calcular Desconto\n3-Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        compra = float(input("Digite o valor da compra: "))
        frete = float(input("Digite o valor do frete: "))
        print(funcoes.calcular_frete(compra, frete))
    elif opcao == 2:
        compra = float(input("Digite o valor da compra: "))
        print("obs: (10% = 0.1, 20% = 0.2, 30% = 0.3...): ")
        desconto = float(input("Digite o valor do desconto(opcional): "))
        print(funcoes.aplicar_desconto(compra, desconto))
    elif opcao == 3:
        break
    else:
        print("Opção inválida")

