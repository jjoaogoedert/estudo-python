sexo = str(input("Informe seu sexo [M/F] : ")).strip().upper()[0] #feito input do tipo string, onde foi retirado os espaços do começo e fim da string, e alterado para caixa alta, e pega somente a priemira letra com o [0]
while "F" != sexo != "M":
    sexo = str(input("Dados inválidos, digite novamente, [M/F] : ")).strip().upper()[0]
print("Dados corretos")