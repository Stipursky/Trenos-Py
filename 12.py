consumo = int(input("Insira a faixa kWh consumida: "))
tipo = input("Insira o tipo de instalação em 'R', 'C' ou 'I': ")

match tipo:
    case 'R':
        if consumo >= 500:
            preço = 0.40
        else:
            preço = 0.65
    case 'C':
        if consumo >= 1000:
            preço = 0.55
        else:
            preço = 0.60
    case 'I':
        if consumo >= 5000:
            preço = 0.55
        else:
            preço = 0.60

total = consumo * preço

print(f"O preço total a pagar é de R${total:.2f}.")