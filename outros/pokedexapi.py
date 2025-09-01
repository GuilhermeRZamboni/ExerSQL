import requests

def buscar_pokemon(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        return {
            "nome": dados["name"].capitalize(),
            "tipo": [t["type"]["name"] for t in dados["types"]],
            "hp": dados["stats"][0]["base_stat"],
            "ataque": dados["stats"][1]["base_stat"]
        }
    else:
        return None

pokemons = {}
pc = {}

print("Programa Pokédex com API!")
while True:
    print("\n1 - Consultar pokemons na mochila")
    print("2 - Capturar pokemon")
    print("3 - Enviar pokemon para o PC")
    print("4 - Trazer pokemon do PC")
    print("5 - Consultar PC")
    print("6 - Quantidade de pokemons capturados")
    print("7 - Checar média dos pokemons da mochila")
    print("8 - Encerrar programa")
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        if pokemons:
            for nome in pokemons:
                print(nome)
            nome = input("Ver status de qual pokemon? (ou 0 para voltar): ").capitalize()
            if nome in pokemons:
                print(pokemons[nome])
        else:
            print("Nenhum pokemon na mochila.")
    elif opcao == "2":
        nome = input("Digite o nome do pokemon para capturar: ").strip().lower()
        poke = buscar_pokemon(nome)
        if poke:
            if len(pokemons) >= 6:
                print("Limite de 6 pokemons na mochila. Enviando para o PC.")
                pc[poke["nome"]] = poke
            else:
                pokemons[poke["nome"]] = poke
                print(f"{poke['nome']} capturado!")
        else:
            print("Pokemon não encontrado na API.")
    elif opcao == "3":
        if pokemons:
            for nome in pokemons:
                print(nome)
            nome = input("Qual pokemon enviar para o PC? ").capitalize()
            if nome in pokemons:
                pc[nome] = pokemons[nome]
                del pokemons[nome]
                print(f"{nome} enviado para o PC.")
            else:
                print("Pokemon não encontrado na mochila.")
        else:
            print("Nenhum pokemon na mochila.")
    elif opcao == "4":
        if pc:
            for nome in pc:
                print(nome)
            nome = input("Qual pokemon trazer do PC? ").capitalize()
            if nome in pc:
                if len(pokemons) >= 6:
                    print("Mochila cheia! Remova um pokemon antes.")
                else:
                    pokemons[nome] = pc[nome]
                    del pc[nome]
                    print(f"{nome} movido para a mochila.")
            else:
                print("Pokemon não encontrado no PC.")
        else:
            print("PC vazio.")
    elif opcao == "5":
        if pc:
            for nome in pc:
                print(nome)
            nome = input("Ver status de qual pokemon do PC? (ou 0 para voltar): ").capitalize()
            if nome in pc:
                print(pc[nome])
        else:
            print("PC vazio.")
    elif opcao == "6":
        print(f"Total de pokemons capturados: {len(pokemons) + len(pc)}")
    elif opcao == "7":
        if pokemons:
            total_hp = sum(p["hp"] for p in pokemons.values())
            total_ataque = sum(p["ataque"] for p in pokemons.values())
            print(f"Média de HP: {total_hp/len(pokemons):.2f}")
            print(f"Média de ataque: {total_ataque/len(pokemons):.2f}")
        else:
            print("Nenhum pokemon na mochila.")
    elif opcao == "8":
        print("Encerrando programa. Obrigado por usar!")
        break
    else:
        print("Opção inválida.")
