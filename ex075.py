i = posicao = nove = numTres = 0
numeros = numeroPar = ()

while i < 4:
    numero = int(input("Digite um numero: "))
    numeros = numeros + (numero,)
    i += 1

for posicao in numeros:
    if posicao == 9:
        nove += 1
    if posicao == 3:
        numTres = posicao
    if posicao % 2 == 0:
        numeroPar +=  (posicao,)
print("O quantidade de numeros nove digitados foi {}".format(nove))
print("O primeiro numero 3 digitado foi na posição {}".format(numTres))
print("Os numeros pares foram {}".format(numeroPar))