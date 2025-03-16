ano = int(input("Digite um ano: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano que vc digitou, {} é bixxesto".format(ano))
else:
    print("O ano que vc digitou, {} não é bixxesto".format(ano))