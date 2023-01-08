def validas_opcoes(opcoes_validas):
    opcoes = opcoes_validas.lower()
    while True:
        escolha = input("Escolha sua opção: ")
        if escolha.lower() in opcoes:
            break

        print("Opção invalida! Digite novamente. \n")
    
    return escolha

opcoes_validas = 'ABCDEF'
print(f"A opção {validas_opcoes(opcoes_validas)} é válida.")