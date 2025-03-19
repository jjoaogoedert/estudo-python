menorPeso = float("inf") #esse valor é um valor muito alto, usado para comparar sempre o menor peso
maiorPeso = 0

for i in range(1,6): #float para percorrer de até 5
    peso = float(input(f"Peso da {i} pessoa: "))
    if peso > maiorPeso: #valida se o peso é maior que a variavel de maiorPeso
        maiorPeso = peso #realiza atribuição
    if peso < menorPeso: #valida se a variavel peso é menor que menorPeso
        menorPeso = peso #realiza atribuição
print("O maior peso digitado foi {}".format(maiorPeso)) #print na tela
print("O menor peso digitado foi {}".format(menorPeso)) #print na tela