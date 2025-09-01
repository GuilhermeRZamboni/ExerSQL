# #criando um afunção
# def nome_da_funcao():
#     print("Olá, mundo")

# # # Chamar a função 
# # nome_da_funcao()

# #funções com parâmetro
# def saudacao(nome):
#     print(f"Ola {nome}")
# #Argumento
# # saudacao(input("Digite seu nome: "))

# #def nome_da_função(parâmetro[valor necessario para a ]):
#     #proceso ou codigo

# #nome_da_funcao(argumento[valor real do parametro na função]



# def tradutor_girias(giria):
#     if giria.lower() == "lobeca":
#         return "cabelo"
#     elif giria.lower() == "masseiro":
#         return "Mentiroso"
#     elif giria.lower() == "moscando":
#         return "Ta viajando/perdido"



# import requests
# import json

# def conversor(valor, taxa):
#     print(f"O valor R$ {valor} convertido é: $ {valor / taxa}")

# cotacoes = requests.get("https://economia.awesomeapi.com.br/json/daily/USD-BRL/30")
# dados = cotacoes.json()

# with open ("dados.json", "w", encoding="utf-8") as arquivo:
#     json.dump(dados, arquivo, indent=4)

# cota_atual = dados[0]["bid"] 
# float(cota_atual)
# conversor(float(input("Digite o valor (R$) que você quer converter: ")), float(cota_atual))


import operacao  as op


total_soma = op.soma(10, 20, 30, 40)
print(f"A soma é: {total_soma}")

total_subtracao = op.subtracao(100, 50)
print(f"A subtração é: {total_subtracao}")

media = op.media(10, 20, 30, 40)
print(f"A média é: {media}")    

