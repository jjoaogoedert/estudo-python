numero = int(input("Digite um numero"))
i = 1
tabuada = 0

while i < 10:
    tabuada = numero * i
    print("A tabuada do numero {} vezes {} é: {}".format(numero,i,tabuada))
    i += 1