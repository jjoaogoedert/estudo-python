distancia = int(input("Digite a distancia da sua viagem em km: "))

if distancia > 200:
    total = distancia * 0.45
else:
    total = distancia * 0.50

print("Vc está prestes a começar a sua viagem de {:.1f}km.".format(distancia))
print("O valor da sua passagem é: R${:.2f}.".format(total))