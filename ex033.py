n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

if n1 > n2 and n2 > n3:
    print("O primeiro numero é o maior")
elif n2 > n3 and n3 > n1:
    print("O segundo numero é o maior")
else:
    print("O terceiro numero é o maior")

if n1 < n2 and n2 < n3:
    print("O primeiro numero é o menor")
elif n2 < n3 and n3 < n1:
    print("O segundo numero é o menor")
else:
    print("O terceiro numero é o menor")