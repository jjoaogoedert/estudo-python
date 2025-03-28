continua = ''
totalMais18 = totalHomem = totalMulher = 0

while continua != 'N':
    print('-' * 50)
    print('Cadastre uma pessoa')
    print('-' * 50)
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo[M/F]: ")).upper().strip()[0]
    if idade > 18:
        totalMais18 += 1
    if sexo == 'M':
        totalHomem += 1
    if sexo == 'F' and idade < 20:
        totalMulher += 1
    continua = str(input("Vc quer continuar?[S/N]: ")).upper().strip()[0]
print("Total de pessoas com mais de 18 anos {}".format(totalMais18))
print("Total de pessoas homens {}".format(totalHomem))
print("Total de pessoas mulheres com mais de 20 anos {}".format(totalMulher))



######################## outra forma de fazer
idade2 = totalMais182 = totalHomem2 = totalMulher2 = 0

while True:
    print('-' * 50)
    print('Cadastre uma pessoa')
    print('-' * 50)
    idade2 = int(input("Digite a idade: "))
    sexo2 = ' '
    while sexo2 not in "MF":
        sexo2 = str(input("Digite o sexo[M/F]: ")).upper().strip()[0]
    if idade2 > 18:
        totalMais182 += 1
    if sexo2 == 'M':
        totalHomem2 += 1
    if sexo2 == 'F' and idade2 < 20:
        totalMulher2 += 1
    resposta = ' ' #Foi necessário adicioonar uma string vazia, para garantir que o programa não de erro, pois pode ser qque um valor errado vai para a variavel, por exemplo, hoje o while pega a posição zero da string, porem se ela estiver vazia não terá a posição zero
    while resposta not in 'SN':
        resposta = str(input("Vc quer continuar?[S/N]: ")).upper().strip()[0]
    if resposta == 'N':
        break
print("Total de pessoas com mais de 18 anos {}".format(totalMais182))
print("Total de pessoas homens {}".format(totalHomem2))
print("Total de pessoas mulheres com mais de 20 anos {}".format(totalMulher2))

