# Este módulo contém funções básicas de matemática

def soma(*valores):
    return sum(valores)

def subtracao(n1, n2):
    return n1 - n2

def media(*numeros):
    return sum(numeros) / len(numeros) if numeros else 0
