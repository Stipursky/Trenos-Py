deposito = float(input("Insira o depósito inicial: "))
taxa = float(input("Insira a taxa de juros (em porcentagem): "))
mes = 1
saldo = deposito
while mes <= 24:
    saldo = saldo + (saldo * (taxa / 100))
    print(f"No mês {mes} o saldo é de R${saldo:.2f}.")
    mes += 1
print(f"\nOs lucros com juros foram de R${saldo - deposito:.2f}.")