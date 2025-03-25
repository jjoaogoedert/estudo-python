escolha = ''
cont = numero = total = maior = menor = 0

while escolha.upper() != 'N':
    numero = int(input("Digite um numero: "))
    total += numero
    cont += 1
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    escolha = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]

media = total / cont
print("A media dos numeros ficou: {}".format(media))
print("O maior numero {} e o menor numero {}".format(maior,menor))