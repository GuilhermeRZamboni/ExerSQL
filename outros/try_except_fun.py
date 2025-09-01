import time
biblioteca = {
    1: {"titulo": "Python Básico",
         "autor": "Gabriel",
        "disponivel": True},
    2: {"titulo": "Lógica de Programação",
         "autor": "Valdinei",
        "disponivel": False},
    3: {"titulo": "Algoritmos",
        "autor": "James", 
        "disponivel":True}
    }



def menu(opcao, opcao_validas = [1, 2, 3, 4, 5]):

    print(f"{"-" * 30} \n1-Consultar livro\n2-Adicionar livro\n3-Atualizar livro\n4-Deletar livro\n5-Sair\n{"-" * 30}")
    opcao = int(input("Digite a opção desejada: "))
    try:
        if opcao in opcao_validas:
            return opcao
        else:
            raise KeyError
    except ValueError:
        print("Opção inválida, digite um número")
    except KeyError:
        print("Opção invalida, digite apenas uma das opções do menu")


def consultar_livro(id):
    try:
        print(biblioteca[id])

    except KeyError:
        print("Livro não encontrado")

    finally:
        print("Voltando ao menu...")
        time.sleep(1)

# Adicionar
def adicionar_livro(id):
    try:
        biblioteca[id]
        print("ID já existe, tente outro")
        
    except KeyError:
            biblioteca[id] = {"titulo": input("Digite o título do livro: "),
                    "autor": input("Digite o autor do livro: "), 
                    "disponivel":True}
            print("Livro adicionado com sucesso")
    finally:
        print("Voltando ao menu...")
        time.sleep(1)

# Atualizar
def atualizar_livro(id):
    try:
        biblioteca[id]
    except KeyError:
        print("ID não encontrado")
    else: 
        biblioteca[id] = {"titulo": input("Digite o título do livro: "),
                        "autor": input("Digite o autor do livro: "), 
                        "disponivel":True}
        print("Livro atualizado com sucesso")
    finally:
        print("Voltando ao menu...")
        time.sleep(1)
# Deletar
def deletar_livro(id):
    try:
        del biblioteca[id]
        print("Livro deletado com sucesso")
    except KeyError:   
        print("Livro não encontrado")
    finally:
        print("Voltando ao menu...")
        time.sleep(1)


