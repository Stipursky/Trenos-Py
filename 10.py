total, count, media_turma, soma = 5, 1, 0, 0
while count <= total:
    nome = input("Insira o nome do aluno: ")
    n1 = float(input("Insira a 1ª nota: "))
    n2 = float(input("Insira a 2ª nota: "))
    media = (n1 + n2) / 2
    if media >= 7:
        print(f"O aluno(a) {nome} foi aprovado(a) com média {media: .2f}.")
    else:
        print(f"O aluno(a) {nome} foi reprovado(a) com média {media: .2f}.")
    soma += media
    count += 1

media_turma = soma / total
print(f"A média da turma foi de {media_turma: .2f}.")