import math

numero = float(input("Digite um numero"))

total = math.trunc(numero)

print("A parte inteira do numero que vc digitou é:",int(total))

# outra forma de fazer sem a importação do modulo math

numero2 = float(input("Digite outro numero"))
print("A parte inteira do seu numero {}, é {}".format(numero2,int(numero2)))