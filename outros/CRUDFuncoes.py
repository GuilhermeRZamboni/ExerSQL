import time
def menu():
    print("------MENU------\n1 - Listar Produtos\n2 - Adicionar Produto\n3 - Atualizar Produto\n4 - Excluir Produto\n5 - Sair")


        
def listar_produtos(produtos):
    if len(produtos) == 0:
        print( "Nenhum produto cadastrado")
        return
    for produto in produtos:
        print(f"-ID: {produto}\n-Nome: {produtos[produto]["nome"]}\n-Preço: R$ {produtos[produto]["preco"]:,.2f}\n-Marca: {produtos[produto]["marca"]}\n")
        time.sleep(0.5)  
    print("Voltando ao menu...")
    time.sleep(1)  
    return

def adicionar_produto(produtos):
    while True:
        nome = input("Digite o nome do produto ou 0 para cancelar: ")
        if nome == "0":
            print("Adição cancelada, voltando ao menu...")
            time.sleep(1)
            return
        preco = input("Digite o preço do produto: ")
        marca = input("Digite a marca do produto: ")
            
        if len(nome.strip()) > 0 and preco.isdigit() and len(marca.strip()) > 0:
            preco = float(preco)
            break
        print("Voce deve digitar o nome e a marca, tente novamente")
    
    for produto in produtos:
        if produtos[produto]["nome"].upper() == nome.upper():
            return "Produto já cadastrado"
    
   
    id = len(produtos) * 100 + 100
    produtos[id] = {"nome":nome,"preco": preco, "marca": marca}
    print(f"Produto {nome} adicionado com sucesso!, voltando ao menu...")
    time.sleep(1)
    return produtos

def atualizar_produto(produtos):
    while True:
        id = input("Digite o id do produto a ser atualizado ou 0 para cancelar: ")
        if not id.isdigit():
            print("ID inválido! Deve ser um número.")
            continue
        else:
            id = int(id)
            
        if id == 0:
            print("Atualização cancelada, voltando ao menu...")
            time.sleep(1)
            return
        if id in produtos:
            nome = input("Digite o novo nome: ").strip().capitalize()
            preco = float(input("Digite o novo preço: "))
            marca = input("Digite a nova marca: ")
            produtos[id] = {"nome":nome, "preco": preco, "marca": marca}
            print(f"ID {id} atualizado com sucesso!, voltando ao menu...")
            time.sleep(1)        
            return
        else:
            print("ID não encontrado, tente novamente")


def excluir_produto(produtos):
    while True:
        id = input("Digite o id do produto a ser excluído ou 0 para voltar: ")
        if id.isdigit():
            id = int(id)
            if id == 0:
                print("Exclusão cancelada, voltando ao menu...")
                time.sleep(1)
                return
            if id in produtos:
                del produtos[id]
                print(f"ID {id} excluído com sucesso!")
                print("Voltando ao menu...")
                time.sleep(1)   
                return
            else:
                print("ID não encontrado, tente novamente")
        else:
            print("ID invalido, digite apenas numeros!")
        
