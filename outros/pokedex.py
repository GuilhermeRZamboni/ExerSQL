pokemons = {
        "Squirtle":{
            "tipo": "agua",
            "nivel":22,
            "hp":89,
            "ataque":12},
  
        "Kubone": {
            "tipo": "terra",
            "nivel": 32,
            "hp": 110.1,
            "ataque": 27},
 
        "Snorlax":{
            "tipo":"normal",
            "nivel":53,
            "hp":320.3,
            "ataque":32},

        "Lucario": {
            "tipo": "Lutador",
            "nivel": 69,
            "hp": 200.5,
            "ataque": 54}
    }
pc = {}
print("Programa Pokedéx: ")
while True:
    print("\n1 - consultar pokemons")
    print("2 - cadastrar pokemon")
    print("3 - excluir pokemon ou envia-lo ao pc")
    print("4 - trazer o pokemon do pc")
    print("5 - Colsultar PC")
    print("6 - Quantidade de pokemons Capturado")
    print("7 - Checar média dos seus pokemons da sua bolsa!")
    print("8 - Encerrar programa" )
    opcao = input("Qual opção você deseja escolher?: ").strip()
    if opcao == "1":
        for pokemon in pokemons:
            print(pokemon)
        while True:
            pergunta_status = input("Qual pokemon você deseja ver o status? (ou 0 se não quiser ver os status): ").strip().capitalize()
            if pergunta_status != "0":
                if pergunta_status in pokemons:
                    print(pokemons[pergunta_status])
                    break
                else: 
                    print("Pokemon não encontrado")
            else:
                print("Ok, voltando ao Menu...")
                break
    elif opcao == "2":
        while True:
            novo_pokemon = input("Qual pokemon você deseja cadastrar? ou 0 para voltar para o menu: ").capitalize().strip()
            if novo_pokemon != "0":
                if novo_pokemon in pokemons:
                    print("Pokemon Existente, tente novamente")
                else:
                    break
            else: 
                break
        
        tipo = input("Qual o tipo do pokemon?: ")
        nivel = int(input("Qual o nivel do pokemon?: "))
        hp = int(input("Qual o hp do pokemon?: "))
        ataque = int(input("Qual o ataque do pokemon?: "))
        if len(pokemons) >= 6 :
            pc[novo_pokemon] = {"tipo": tipo, "nivel": nivel, "hp":hp, "ataque" : ataque}
            print("Opa limite de pokemons atingido (6), enviando o pokemon ao pc")
        else:
            print("Pokemon Capturado !!!🌟")
            while True:
                pc_ou_mochila = input("Você deseja adicionar o pokemon ao pc ou deixa-lo na mochila? (pc/mochila)")
                if pc_ou_mochila == "pc":
                    pc[novo_pokemon] = {"tipo": tipo, "nivel": nivel, "hp":hp, "ataque" : ataque}
                    print("Pokemon guardado no pc!!!")
                    break
                elif pc_ou_mochila == "mochila":
                    pokemons[novo_pokemon] = {"tipo": tipo, "nivel": nivel, "hp":hp, "ataque" : ataque}  
                    print("Pokemon já esta na sua mochila e pronto para uso!")   
                    break
                else:
                    print("Comando inválido! (pc/mochila)")
    elif opcao == "3":
        while True:
            excluir_ou_pc = input("Você deseja excluir o pokemon ou enviar para ao pc (excluir/enviar): ").strip().lower()
            if excluir_ou_pc != "excluir" and excluir_ou_pc != "enviar":
                print("Comando não entendido, digite (excluir/enviar)")
            else:
                break
        if excluir_ou_pc == "enviar":
            while True:
                for pokemon in pokemons:
                    print(pokemon)
                enviar_pc = input("Qual pokemon você deseja enviar para o pc?: ").strip().capitalize()
                if enviar_pc in pokemons:
                    pc[enviar_pc] = pokemons[enviar_pc]
                    del pokemons[enviar_pc]
                    print("Pokemon enviado com sucesso!\nVoltando ao menu...")
                    break
                else:
                    print("Pokemon não encontrado ou já está no pc")
        
        elif excluir_ou_pc == "excluir":
            while True:
                excluir = input("Qual pokemon você deseja excluir?: ")
                if excluir in pokemons:
                    del pokemons[excluir]
                    print("Pokemon excluido")
                    break
                elif excluir in pc:
                    del pc[excluir]
                    print("Pokemon excluido do pc")
                    break
                else:
                    print("Pokemon não encontrado")
    elif opcao == "4":
        
        if len(pc)>0:
            for pokemon in pc:
                print(pokemon)
            while True:
                pokemon_alterado = input("Qual pokemon você deseja trazer do pc?: ")
                if pokemon_alterado in pc:
                    if len(pokemons) >= 6:
                        substituir = input("Opa limite de pokemons atingido (6), você deseja substituir algum? (s/n): ").strip().lower()
                        if substituir == "s":
                            pokemon_substituido = input("Qual pokemon você deseja substituir?: ")
                            if pokemon_substituido in pokemon:
                                pc[pokemon_substituido] = pokemons[pokemon_substituido]
                                del pokemons[pokemon_substituido]
                                pokemons[pokemon_alterado] = pc[pokemon_alterado]
                                del pc[pokemon_alterado]
                                print("Pokemon alterado com sucesso!!\nVoltando para o menu...")
                                break
                            else:
                                print("Pokemon não encontrado!")
                                continue
                        else:
                            print("Ok, Voltando para o menu...")
                            break
                    else:
                        pokemons[pokemon_alterado] = pc[pokemon_alterado]
                        del pc[pokemon_alterado]
                        print("Pokemon ja está pronto para uso\nVoltando para o menu...")
                        break
                else:
                    print("Pokemon não encontrado, tenha certeza que ele está no seu pc")
        else:
            print("Não existe nenhum pokemon no seu pc\nVoltando para o menu...")
    elif opcao == "5":
        if len(pc) > 0:
            print("Aqui esta os pokemons do seu pc!")
            for pokemon in pc:
                print(pokemon)
                while True:
                    pergunta_status = input("Qual pokemon você deseja ver o status? (ou 0 se não quiser ver os status): ").strip().capitalize()
                    if pergunta_status != "0":
                        if pergunta_status in pc:
                            print(pc[pergunta_status])
                            break
                        else: 
                            print("Pokemon não encontrado")
                    else:
                        print("Ok, voltando ao Menu...")
                        break
        else:
            print("Não existe nenhum pokemon no seu pc\nVoltando para o menu...")
    elif opcao =="6":
        print(f"Você capturou {len(pc) + len(pokemons)} pokemons!! Parabéns treinador!!")
    elif opcao == "7":
        total_hp = 0
        total_ataque = 0
        total_nivel = 0
        for pokemon in pokemons:
            total_hp += pokemons[pokemon]["hp"]
            total_ataque += pokemons[pokemon]["ataque"]
            total_nivel += pokemons[pokemon]["nivel"]
        print(f"Média de HP: {total_hp/len(pokemons):.2f}")
        print(f"Média de ataque: {total_ataque/len(pokemons):.2f}")
        print(f"Média de nivel: {total_nivel/len(pokemons):.2f}")
    elif opcao == "8":
        print("Parando programa, Obrigado por usar...")
        break
    
    else:
        print("Opção inválida")
print("Obrigado por usar o programa")
