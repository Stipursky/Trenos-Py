total = 0
while True:
    codigo = int(input("Insira o código do produto (0 para concluir): "))
    match codigo:
        case 0:
            break
        case 1:
            preço = 0.50
        case 2:
            preço = 1.00
        case 3:
            preço = 4.00
        case 5:
            preço = 7.00
        case 9:
            preço = 8.00
        case _:
            print("Código inválido.")
            continue
    
    quantidade = int(input("Insira a quantidade desejada: "))
    total = total + (quantidade * preço)
print(f"O valor a ser pago é de R${total:.2f}")