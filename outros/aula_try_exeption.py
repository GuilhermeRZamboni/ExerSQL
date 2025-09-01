# Trabalhando com try e except

# SyntaxError - erro de escrita
# numero = 10
# # texto = "Olá, mundo

# if numero > 10
#     print("O número é maior que 10")

# Indentation - Erro de indentação
# soma = lambda n1, n2: n1 + n2
# total = soma(10,98)
#  print(f"O resultado da soma é {total}")

# for i in range(5):
# print(i)

# Key error - erro de chave inexitente
# estoque = {"código": 1, "nome": "Davi", "telefone": "4002-8922"}

# print(estoque["Nome"])
# print(estoque["celular"])

# #NameError - quando a variável não foi declarada

# X = 10
# y = 20

# print(f"O resultado da soma é {X + y}")

# def media(*notas):
#     return sum(notas) / len(notas)
# resultado = media_total(10, 8, 9, 7)

#ValueError - valor fora do intervalo certo
# print(int(5.75))
# print(int("38"))
# print(int("dez"))


# #indexEroor - índice fora do intervalo
#lista, tupla, string e dicionario
# lista = [10, 20, 30, 40, 50]
# print(lista[5])


# #ZeroDivisionError - divisão por zero
# numero = int(input("Digite um número: "))
# soma = 10 + numero
# resultado = soma / numero
# print(f"O resultado é {resultado}")

# #try e except
# #tratando exeções
# try:
#     numero = int(input("Digite um número: "))
#     soma = 10 + numero
#     resultado = soma / numero
#     print(f"O resultado é {resultado}")
# except ZeroDivisionError:
#     print("Nao pode dividir por zero")
# except ValueError:
#     print("Valor inválido, digite um número inteiro")
# else:
#     print("Não deu erro!")
# finally:
#     print("Esta linha sempre será executada")


#Procurar um produto no estoque
estoque = {"caneta": 10, "lapis": 20, "caderno": 15}
def buscar_estoque(produto):
    try:
        return f"O estoque de {produto} é {estoque[produto]} unidades"
    except KeyError:
        return f"O produto {produto} não foi encontrado no estoque"
    
for produto in estoque:
    print(produto)
print(buscar_estoque(input("Digite o nome do produto: ").lower()))