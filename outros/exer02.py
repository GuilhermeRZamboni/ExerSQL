def apresentar(nome, sobrenome=False):
    if sobrenome:
        print(f"Olá {nome} {sobrenome}!")
    else:
        print(f"Olá {nome}!")

apresentar(input("Digite seu nome: "),  input("Digite seu sobrenome(opcional)"))


#Desempacotando parâmetros
def calcular_media(*notas):
    if notas:
        media = sum(notas) / len(notas)
        return f"{media:.1f}"
    else:
        return "Nenhuma nota informada."

print(calcular_media(10, 9, 8, 5, 6, 7, 9))


def soma(n1, n2):
    return n1 + n2

def multi(n1, n2):
    return n1 * n2

def calcular(funcao, n1, n2):
    return funcao(n1, n2)

total_soma = calcular(soma, 53, 20)
print(total_soma)



print(f"{range(1, 10000000000000000)}")  # Gera números de 1 a 9

# Este módulo contém funções básicas de matemática

def soma(*valores):
    return sum(valores)

def subtracao(n1, n2):
    return n1 - n2

def media(*numeros):
    return sum(numeros) / len(numeros) if numeros else 0
