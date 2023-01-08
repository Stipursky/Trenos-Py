numeros = []

for _ in range(10):
    num = int(input(f"Insira o {_+1}º numero."))
    numeros.append(num)

count = 0
ultimo = numeros[9]

for num in numeros:
    if num == ultimo:
        count += 1

print(f"O número {ultimo} foi repetido {count} vezes.")