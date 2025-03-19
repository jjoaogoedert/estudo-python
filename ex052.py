numero = int(input("Digite um numero: "))

for i in range(1,numero + 1):
    if numero % i == 0:
        print("\033[33m{}".format(i),end=" ")
    else:
        print("\033[31m{}".format(i),end=" ")

