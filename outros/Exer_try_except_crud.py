import try_except_fun as crud
import time


while True:

    opcao = crud.menu(0)
    if opcao == 1:
        id = int(input("Digite o ID do livro: "))
        crud.consultar_livro(id)
    elif opcao == 2:
        id = int(input("Digite o ID do livro: "))

        crud.adicionar_livro(id)
    elif opcao == 3:
        id = int(input("Digite o ID do livro: "))

        crud.atualizar_livro(id)
    elif opcao == 4:
        id = int(input("Digite o ID do livro: "))
        crud.deletar_livro(id)
    elif opcao == 5:
        print("Saindo...")
        break


        