total = 0
i = 0

for controle in range(1,501,2):
    if controle % 3 == 0:
        i += 1
        total += controle
print("O valor de soma de todos os numeros {} multiplos de tres fica {}".format(i,total))