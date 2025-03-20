from math import factorial

numero = int(input("Digite um numero para calcularmos seu fatorial \n"
                   "Digite o numero: "))
contador = 1
fatorial = 1
msg = []

while contador != numero + 1:
    msg.append(contador)
    fatorial = fatorial * numero
    total = factorial(numero)
    contador += 1
arrayInvertido = msg[::-1]
print("Calculando... {}! =".format(numero) ,*arrayInvertido, sep=" x ", end= " = {}".format(total))


######Outra forma de fazer

numero2 = int(input("Digite um numero: "))

c = numero2
fato = 1

print("Calculando ..... {} ! = ".format())
while c > 0:
    print("{} ! = {} x".format(numero2,c), end=" = ")
    fato *= c
    c -= 1

print("{}".format(fato))