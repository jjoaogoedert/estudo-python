from datetime import date

dataAtual = date.today().year #pega a data atual, mas preciso o ano atual
resultado = 0
maiorIdade = 0
menorIdade = 0

for i in range(1,8):
    ano = int(input(f"Digite ano de nascimento da {i} pessoa: "))
    resultado = dataAtual - ano
    if resultado >= 18:
        maiorIdade += 1
    else:
        menorIdade += 1

print("Ao todo tivemos {} pessoas maiores de idade".format(maiorIdade))
print("E tambem tivemos {} pessoas menores de idade".format(menorIdade))