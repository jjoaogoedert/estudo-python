import random
numeros = []
i = position = 0

while i <= 5:
    i += 1
    numeros.append(random.randint(0,11))
print(numeros)

#Outra forma de fazer, onde ele adiciona 5 numeros aleatórios na tupla, inserindo diretamente, porem da outra forma é mais correta, mais eficiente
numeros2 = (
            random.randint(1,11),
            random.randint(1,11),
            random.randint(1,11),
            random.randint(1,11),
            random.randint(1,11)
            )

maior = menor = numeros[0]

for position in numeros:
    if position < menor:
        menor = position
    if position > maior:
        maior = position
print("O menor numero é {}".format(menor))
print("O maior numero é {}".format(maior))