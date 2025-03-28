cont = 0
total = 0

while True:
    numero = int(input("Digite um numero: (999 para parar) "))
    total += numero
    cont += 1
    if numero == 999:
        break

print("A soma desses {} valores, fica {}".format(cont - 1,total - 999))