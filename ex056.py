media = 0
maiorIdade = 0
nomeMaisVelho = ""
mulherMenor = 0
totalPessoas = 4

for i in range(1,totalPessoas + 1):
    print("=" * 10 + " {} pessoa ".format(i) + "=" * 10)
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").upper()
    media = media + idade
    if sexo == "M" and idade > maiorIdade:
        maiorIdade = idade
        nomeMaisVelho = nome
    if sexo == "F" and idade < 20:
        mulherMenor += 1

print("A média de idade do grupo é: {}".format(media / totalPessoas))
print("O homem mais velho é: {}".format(nomeMaisVelho))
print("A quantidade de mulheres menores de 20 anos são {}".format(mulherMenor))