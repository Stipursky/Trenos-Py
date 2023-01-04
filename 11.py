v = int(input("Insira a velocidade do veículo: "))

if v > 80:
    multa = (v - 80) * 5
    print(f"O veículo ultrapassou o limite de velocidade, e foi multado em: R${multa:.2f}.")
else:
    print("O veículo respeitou o limite de velocidade.")