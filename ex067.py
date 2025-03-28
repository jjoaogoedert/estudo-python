cont = total = i = 0

print("-" * 30)

while True:
    numero = int(input("Digite um valor para saber a tabuada (negativo para sair): "))
    if numero < 0:
        break
    for i in range(1,11):
        total = numero * i
        print("{} X {} = {}".format(numero,i,numero * i))

print("-" * 30)
print("FIM")