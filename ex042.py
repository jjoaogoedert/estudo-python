r1 = float(input("Digite a primeira reta"))
r2 = float(input("Digite a segunda reta"))
r3 = float(input("Digite a terceira reta"))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 == r3:
        tipo = "EQUILÁTERO"
    elif r1 != r2 != r3 != r1:
        tipo = "ESCALENO"
    else:
        tipo = "ISÓSCELES"
    print("As retas podem formar um triangulo do tipo {}".format(tipo))
else:
    print("As retas não podem formar um triangulo")