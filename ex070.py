nome = prodBarato = ''
valor = cont = total = maiorMil = maisBarato = 0
resposta = ' '

print('*-' * 35)
print("Loja sedorf de produtos diversos:")
print("Menu de inserção:")
print('-' * 70)


while resposta not in 'N':
    nome = str(input("Nome produto: "))
    valor = float(input("Valor do produto: "))
    total += valor
    maisBarato = valor
    if valor > 1000:
        maiorMil += 1
    if valor <= maisBarato:
        prodBarato = nome
    resposta = str(input("Vc quer continuar[S/N]? ")).strip().upper()[0]
print("O valor total dos produtos ficou: R${:.2f}".format(total))
print("Os produtos que custaram mais de R$1000.00 ficou: {}".format(maiorMil))
print("O produto de menor valor é {} com o valor de R${:.2f}".format(prodBarato.upper(),maisBarato))

print('-' * 50)
print("Outra forma de implementar")
print('-' * 50)

nome = prodBarato = ''
valor = cont = total = maiorMil = maisBarato = 0

while True:
    nome = str(input("Nome produto: "))
    valor = float(input("Valor do produto: "))
    total += valor
    maisBarato = valor
    if valor > 1000:
        maiorMil += 1
    if valor <= maisBarato:
        prodBarato = nome
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input("Vc quer continuar[S/N]? ")).strip().upper()[0]
    if resposta == 'N':
        break
print("O valor total dos produtos ficou: R${:.2f}".format(total))
print("Os produtos que custaram mais de R$1000.00 ficou: {}".format(maiorMil))
print("O produto de menor valor é {} com o valor de R${:.2f}".format(prodBarato.upper(),maisBarato))