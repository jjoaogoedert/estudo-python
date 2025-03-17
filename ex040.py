n1 = float(input("Digite a primeira média: "))
n2 = float(input("Digite a segunda média: "))

media = (n1 + n2) / 2

if media >= 7:
    print("Aluno aprovado, com a média {:.2f}".format(media))
elif  6 >= media < 7: #python permite fazer uma condição aninhada dessa forma, onde seria normal fazer com media >= 6 AND media < 7
    print("Aluno está em recuperação, com a média {:.2f}".format(media))
else:
    print("Aluno reprovado, com a média {:.2f}".format(media))
