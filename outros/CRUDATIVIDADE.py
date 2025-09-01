import CRUDFuncoes as cf
estoque = {
100:{
"nome":"Placa de vídeo GTX 1660 ti",
"preco": 950.00,
"marca": "Gygabyte confia"
},
200:{
"nome":"Fone Wireless",
"preco": 50.00,
"marca": "Sonya"
},
}

while True:
    cf.menu()
    opcao = int(input("Digite a opção desejada: "))


    if opcao == 1:
        cf.listar_produtos(estoque)
    elif opcao == 2:
        cf.adicionar_produto(estoque)   
    elif opcao == 3:
        cf.atualizar_produto(estoque)
    elif opcao == 4:
        cf.excluir_produto(estoque)
    elif opcao == 5:
        print("Saindo do sistema...")
        break    
    else:
        print("Opção inválida! Tente novamente.")
        continue