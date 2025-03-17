peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)
print("O IMC dessa pessoa é: {:.1f}".format(imc))
if imc < 18.5:
    print(" Abaixo do Peso")
elif 18.5 <= imc < 25:
    print(" Peso Ideal")
elif 25 <= imc < 30:
    print(" Sobrepeso")
elif 30 <= imc < 40:
    print(" Obesidade")
else:
    print(" Obesidade Mórbida")


