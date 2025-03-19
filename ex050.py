numeros = 0
i = 0
pares = 0

for i in range(1,7):
    num = int(input("Digite um numero para {} : ".format(i)))
    if num % 2 == 0:
        numeros +=  num
        pares += 1
print("A soma dos numeros pares {} que vc digitou: {}".format(pares,numeros))