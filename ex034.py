salario = float(input("Digite seu salário: "))

if salario > 1250.00:
    aumento = salario * 10 / 100
    print("Quem passava a ganhar R${:.2f} vai ganhar agora R${:.2f}".format(salario,aumento+salario))
else:
    aumento = salario * 15 / 100
    print("Quem passava a ganhar R${:.2f} vai ganhar agora R${:.2f}".format(salario, aumento + salario))