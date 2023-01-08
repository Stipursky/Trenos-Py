frutas = {"Banana": 4.00, "Laranja": 3.50, "Limão": 10.00,
          "Maça": 6.50, "Manga": 7.00, "Morango": 8.50,
          "Tangerina": 5.50, "Uva": 12.00}

lista_compras = [('Laranja', 1), ('Morango', 0.5), ('Banana', 0.3),
                 ('Melancia', 2), ('Limão', 0.5), ('Abacaxi', 1.5)]

compras = 0
for fruta, kg in lista_compras:
    if fruta in frutas:
        compras += kg * frutas[fruta]
    else:
        print(f"Fruta Indisponível: {fruta}.")

print(f"O valor total é de: R${compras:.2f}")