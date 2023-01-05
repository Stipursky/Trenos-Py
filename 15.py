lista = [13, 21, 40, 80]
busca = int(input("Insira um valor: "))

for _ in range(len(lista)):
    if busca == lista[_]:
        print("O número pertence a lista.")
        break
    if busca not in lista:
        print("O número não pertence a lista.")
        break