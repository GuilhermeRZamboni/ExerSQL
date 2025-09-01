# Operador condicional ternário
# variavel = resultado_se_verdadeiro if condicao else resultado_se_falso
# idade = 17
# maioridade = "Maior de idade" if idade >= 18 else "Menor de idade"
# print(maioridade)


# numero = int(input("Digite um número: "))
# status = "Par" if numero % 2 == 0 else "Impar"
# print(status)


#[expresao for item in iteravel]

# numeros = []
# for i in range(5):
#     numeros.append(i* 2)
# print(numeros  )

# numeros2 = [i * 2 for i in range(5)]
# print(numeros2)


# pares = []
# for i in range(11):
#     if i % 2 == 0:
#         pares.append(i)
# print(pares)

pares = [i for i in range(11) if i % 2 == 0]
print(pares)