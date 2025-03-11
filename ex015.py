kmPercorrido = float(input("Digite a quantidade de quilometros percorrido no total: "))
diasAlugado = int(input("Digite a quantidade de dias que o carro ficou alugado: "))

total = (diasAlugado * 60) + (kmPercorrido * 0.15)

print("O total que ficou o seu carro é R${:.2f}".format(total))