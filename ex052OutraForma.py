numero = int(input("Digite um numero para sabermos o seus primos: "))
contador = 0

for i in range(1,numero + 1):
    if numero % i == 0:
        contador += 1
        print("\033[33m{}".format(i),end=" ")
    else:
        print("\033[31m{}".format(i),end=" ")

print("\n\033[35mO numero {} foi divisivel {} vezes".format(numero,contador))
if contador == 2:
    print("\033[31mE por isso ele é primo")
else:
    print("E por isso ele não é primo")