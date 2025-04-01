from ex044 import valor

print("*" * 30)
print("Bem vindo ao banco Wolter")
print("-" * 30)
numero = int(input("Qual o valor que vc deseja sacar? "))
total = numero
cedula = 50
totalCed = 0
while True:
    if  total >= cedula:
        total -= 1
        totalCed += 1
    else:
        